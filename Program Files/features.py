from pynput.keyboard import Key, Controller
import time

def scroll(x,y,t,diff):
    keyboard = Controller()
    if y < -10:
        text = "Looking Left"
        keyboard.press(Key.left)
    elif y > 10:
        text = "Looking Right"
        keyboard.press(Key.right)
    elif x < -10:
        text = "Looking Down"
        keyboard.press(Key.down)
    elif x > 10:
        text = "Looking Up"
        keyboard.press(Key.up)
        # count_up+=1                
        # ges.node_up(count_up)
        # time.sleep(1)
    else:
        text = "Forward"
    
    return diff

