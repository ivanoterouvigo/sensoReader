import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Sensor Data Capture Application')
    parser.add_argument('--sensor_type', type=str, required=True, choices=['mockup', 'real'], help='Type of sensor to use')
    parser.add_argument('--interval', type=int, required=True, help='Interval in seconds for reading the sensor data')
    parser.add_argument('--range_min', type=int, required=False, default=0, help='Minimum value for mockup sensor')
    parser.add_argument('--range_max', type=int, required=False, default=65535, help='Maximum value for mockup sensor')
    parser.add_argument('--db_uri', type=str, required=True, help='URI for connecting to the SQL database')
    return parser.parse_args()
