import unittest
from sensor import Sensor

# Class defined from unittest.TestCase
class TestSensor(unittest.TestCase):

    def test_read_data_mockup(self):
        # Sensor instance with min, max
        sensor = Sensor(sensor_type='mockup', range_min=0, range_max=65535)
        
        # read_data from sensor
        data = sensor.read_data()
        
        # Check data len = 64
        self.assertEqual(len(data), 64)
        for value in data:
            # Check value inside (0 to 65535)
            self.assertTrue(0 <= value <= 65535)

if __name__ == '__main__':
    unittest.main()