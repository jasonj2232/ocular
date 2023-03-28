
from pynput.keyboard import Key, Controller
keyboard = Controller()

def node_down(count_down):

    print("d",count_down)
    
    if count_down%2==0:   
        
        keyboard.press(Key.cmd_l)
        keyboard.press('d')
        keyboard.release('d')
        keyboard.release(Key.cmd_l)

def node_up(count_up):
    print("u",count_up)
    
    if count_up%2==0:   
        
        keyboard.press(Key.cmd_l)
        keyboard.press('d')
        keyboard.release('d')
        keyboard.release(Key.cmd_l)
