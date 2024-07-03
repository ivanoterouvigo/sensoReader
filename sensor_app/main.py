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
    
    # Sensor instance
    sensor = Sensor(sensor_type=args.sensor_type, range_min=args.range_min, range_max=args.range_max)
    # DDBB instance by URI
    db = Database(db_uri=args.db_uri)
    nats_client = NATSClient()

    # Connect to server NATS client
    await nats_client.connect()

    # Async function to catch data sensor
    async def capture_data():
        while True:
            data = sensor.read_data()
            db.insert_data(pickle.dumps(data))
            await nats_client.publish("sensor.data", pickle.dumps(data))
            logging.info(f"Data captured and published: {data}")
            # Interval time checking before data capture
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
