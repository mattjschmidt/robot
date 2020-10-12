from gamepad.padService import PadService
import os

def main():

    padServ = PadService()
    padsCopy = padServ.pads.copy()

    while(True):
        while(len(padServ.main) == 0):
            if padsCopy != padServ.pads:
                os.system('clear')
                print('Available Controllers:')
                padsCopy = padServ.pads.copy()
                print(padsCopy)
        newPad = padServ.main[0]
        inputCopy = newPad.input.copy()
        while(len(padServ.main) > 0):
            if inputCopy != newPad.input:
                os.system('clear')
                print(newPad.name)
                inputCopy = newPad.input.copy()
                print(newPad.input)
        main()


        
main()


