from Device import Device
from SmartLight import SmartLight
from SecurityCamera import SecurityCamera
from Thermostat import Thermostat
import random



class AutomationSystem:
    def __init__(self):
        self.__devices = []

    def get_devices(self):
        return self.__devices

    def discover_device(self):
        sl = SmartLight(0)
        t = Thermostat(1)
        sc = SecurityCamera(2)

        self.__devices.append(sl)
        self.__devices.append(t)
        self.__devices.append(sc)


    def randomizing(self):
        for dev in self.__devices:
            self.__devices[0].set_brightness(random.randint(0, 100))
            self.__devices[1].set_temperature(random.randint(10, 100))
            self.__devices[2].detect_motion(True if random.randint(0, 1) else False)

    def randomize_detect_motion(self):
        for dev in self.__devices:
            if(isinstance(dev, SecurityCamera)):
                dev.detect_motion(True if random.randint(0,1) else False)

