#!/bin/env python3

from evdev import InputDevice
from enum import Enum

class SourceType(Enum):
    USB = 1
    BLUETOOTH = 2
    NETWORK = 3

class Controller(object):
    def __init__(self, source, sourceType):
        self.source = source
        self.sourceType = sourceType
        self.ctrl = InputDevice(source)
        self.name = self.ctrl.name
    
    def __str__(self):
        return "Name: " + self.name



