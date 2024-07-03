import asyncio
import logging
import pickle
from config import parse_arguments
from sensor import Sensor
from database import Database
from nats_client import NATSClient

logging.basicConfig(level=logging.INFO)

async def main():
    args = parse_arguments()
    
    sensor = Sensor(sensor_type=args.sensor_type, range_min=args.range_min, range_max=args.range_max)
    db = Database(db_uri=args.db_uri)
    nats_client = NATSClient()

    await nats_client.connect()

    async def capture_data():
        while True:
            data = sensor.read_data()
            db.insert_data(pickle.dumps(data))
            await nats_client.publish("sensor.data", pickle.dumps(data))
            logging.info(f"Data captured and published: {data}")
            await asyncio.sleep(args.interval)

    async def start_capture():
        await capture_data()

    try:
        await start_capture()
    except asyncio.CancelledError:
        logging.info("Data capture stopped.")
    finally:
        db.close()
        await nats_client.close()

if __name__ == '__main__':
    asyncio.run(main())
