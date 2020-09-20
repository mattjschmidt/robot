import evdev
from evdev import InputDevice, categorize, ecodes
from controller import Controller, SourceType
import time
import threading

class Thread(threading.Thread):
    def __init__(self, pad):
        threading.Thread.__init__(self)
        self.pad = pad
    def run(self):
        padSwap(self.pad)
        

def padSwap(pad):
    for event in pad.ctrl.read_loop():
        if event.code == 315 and event.value == 1:
            print("Connected: " + pad.name)

def main():
    printCount = 0
    threads = []
    while(True):
        controllers = [Controller(path, SourceType.USB) for path in evdev.list_devices()]
        if len(controllers) > 0:
            printCount = 0
            for pad in controllers:
                if len(threads) > 0:
                    exists = False
                    for thrd in threads:
                        if pad.source == thrd.pad.source:
                            exists = True
                    if exists == False:
                        padThread = Thread(pad)
                        print("Available device: " + pad.name)
                        threads.append(padThread)
                        padThread.start()
                else: 
                    padThread = Thread(pad)
                    print("Added device: " + pad.name)
                    threads.append(padThread)
                    padThread.start()
        else:
            if printCount == 0:
                print("Please connect a controller to continue...")
                printCount = 1
main()


