

class Device:
    def __init__(self, device_id):
        self._device_id = device_id
        self._status = False

    def get_status(self):
        return self._status

    def tumbler_change(self):
        self._status = not self._status

    def get_id(self):
        return self._device_id

