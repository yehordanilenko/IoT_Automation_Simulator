from Device import Device
import random
import time

class SecurityCamera(Device):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.__security_status = False
        self.__motion = False

    def get_security_status(self):
        return self.__security_status


    def get_motion(self):
        if not self._status:
            return False

        return self.__motion

    def detect_motion(self, motion):
        if not self._status:
            self._status = True

        self.__motion = motion

