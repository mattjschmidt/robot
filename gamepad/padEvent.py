
class PadEvent(object):
    def __init__(self, code, value):
        self.code = code
        self.value = value
    def __repr__(self):
        return 'Code: ' + str(self.code) + ' Value: ' + str(self.value)
    def __eq__(self, other):
        if self.code == other.code and self.value == other.value:
            return True
        else:
            return False
