#from pynput.mouse import Controller
# From left to right , top to bottom
# from top -left of the screen you can imagine  the top-left to be (0,0)
from pynput.keyboard import Controller
def controlMouse():
    mouse= Controller()
    mouse.position=(100,500)
controlMouse()

def controlKeyboard():
    keyboard= Controller()
    keyboard.type("potty my favourite")
controlKeyboard()





