import evdev
from gamepad.pad import Pad
from gamepad.connType import ConnectionType
from gamepad.padServiceThread import PadServiceThread

class PadService(object):
    def __init__(self):
        self.pads = []
        self.main = []
        self.thread = PadServiceThread(self.pads, self.main)
        self.thread.start()

