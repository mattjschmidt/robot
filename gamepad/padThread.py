import threading
from evdev import ecodes
from gamepad.padEvent import PadEvent

class PadThread(threading.Thread):
    def __init__(self, dev, input):
        threading.Thread.__init__(self)
        self.dev = dev
        self.input = input
    def run(self):
        try:
            for event in self.dev.read_loop():
                padEv = PadEvent(event.code, event.value)
                for item in self.input:
                    if item.code == padEv.code:
                        self.input.remove(item)
                if not padEv.value == 0:
                    self.input.append(padEv)
        
        except FileNotFoundError:
            pass

        except OSError:
            pass

        except:
            raise
