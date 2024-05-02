from Device import Device
import random
import time

class Thermostat(Device):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.__temperature = 15

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        if self._status == False:
            self._status = True
        self.__temperature = temperature


