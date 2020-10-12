import threading
import evdev
from evdev import InputDevice
from gamepad.pad import Pad
from gamepad.connType import ConnectionType

class PadServiceThread(threading.Thread):
    def __init__(self, pads, main):
        threading.Thread.__init__(self)
        self.pads = pads
        self.main = main

    def scanConnectedPads(self):
        try:
            paths = evdev.list_devices()
            for path in paths:
                if len(self.pads) > 0:
                    created = False
                    for pad in self.pads:
                        if pad.source == path:
                            created = True
                    if created == False:
                        self.pads.append(Pad(path, ConnectionType.LOCAL))
                else:
                    self.pads.append(Pad(path, ConnectionType.LOCAL))
            for pad in self.pads:
                if not paths.__contains__(pad.source):
                    self.pads.remove(pad)
        except:
            raise

    def switchControl(self):
        if len(self.pads) > 0:
            for pad in self.pads:
                for inp in pad.input:
                    if inp.code == 316:
                        if len(self.main) == 0:
                            self.main.clear()
                            self.main.append(pad)
                        else:
                            self.main.clear()

    def run(self):
        while(True):
            self.scanConnectedPads()
            self.switchControl()
