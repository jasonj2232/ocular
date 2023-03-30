from pynput.keyboard import Key, Controller
import pyautogui
keyboard = Controller()

def gestures(x, y, z):
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
    else:
        text = "Forward"

def click(noOfClicks):
    if noOfClicks==1:
        pyautogui.click()

    if noOfClicks==2:
        pyautogui.rightClick()


