import evdev
from evdev import InputDevice, categorize, ecodes
from controller import Controller, SourceType
import time

def main():
    printCount = 0
    while(True):
        availableDevs = [InputDevice(path) for path in evdev.list_devices()]
        if len(availableDevs) == 1:
            printCount = 0
            pad = Controller(availableDevs[0].path, SourceType.USB)
            try:
                print("Connected: " + pad.name)
                for event in pad.ctrl.read_loop():
                    if (event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS) and event.value == 1:
                        if event.code == 304:
                            print("A")
                        if event.code == 305:
                            print("B")
            except:
                throw
        elif len(availableDevs) > 1:
            if printCount == 0:
                print("Please disconnect any extra controllers to continue...")
                printCount = 1
        elif len(availableDevs) == 0:
            if printCount == 0:
                print("Please connect a controller to continue...")
                printCount = 1
main()


