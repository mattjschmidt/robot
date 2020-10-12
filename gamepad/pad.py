from evdev import InputDevice
from gamepad.padThread import PadThread

class Pad(object):
    def __init__(self, source, sourceType):
        _io = InputDevice(source)
        self.source = source
        self.sourceType = sourceType
        self.name = _io.name
        self.input = []
        self.thread = PadThread(_io, self.input)
        self.thread.start()
    
    def __eq__(self, other):
        if self.source == other.source:
            return True
        else:
            return False

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
