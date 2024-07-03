import unittest
from sensor import Sensor

class TestSensor(unittest.TestCase):

    def test_read_data_mockup(self):
        sensor = Sensor(sensor_type='mockup', range_min=0, range_max=65535)
        data = sensor.read_data()
        self.assertEqual(len(data), 64)
        for value in data:
            self.assertTrue(0 <= value <= 65535)

if __name__ == '__main__':
    unittest.main()