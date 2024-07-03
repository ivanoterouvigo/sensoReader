import random

class Sensor:
    def __init__(self, sensor_type, range_min=0, range_max=65535):
        self.sensor_type = sensor_type
        self.range_min = range_min
        self.range_max = range_max

    def read_data(self):
        if self.sensor_type == 'mockup':
            return [random.randint(self.range_min, self.range_max) for _ in range(64)]
        else:
            # TODO: real sensor reader
            pass