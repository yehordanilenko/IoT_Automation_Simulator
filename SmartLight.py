from Device import Device
import random
import time

class SmartLight(Device):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.__brightness = 0

    def get_brightness(self):
        return self.__brightness

    def set_status(self, status):
        if status == True and self.__brightness == 0:
            self.__brightness = 1
        elif status == False and self.__brightness > 0:
            self.__brightness = 0

        self._status = status

    def set_brightness(self, brightness):
        if self._status == False and brightness > 0:
            self._status = True
        elif self._status == True and brightness == 0:
            self._status = False

        self.__brightness = brightness

    def gradual_dimming(self, steps, duration, delay, step_size):
        for _ in range(steps):
            new_brightness = self.__brightness - step_size
            if(new_brightness >= 0):
                self.__brightness = new_brightness
            time.sleep(delay)

        self.__brightness = 0
        self._status = False
