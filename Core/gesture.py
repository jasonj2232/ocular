from pynput.keyboard import Key, Controller
import pyautogui
import threading
import time
keyboard = Controller()

def gestures(x, y, z):
    countLeft,countRight,countUp,countDown=0,0,0,0

    if y < -10:
        text = "Looking Left"
        #keyboard.press(Key.left)
        countLeft = 1
    elif y > 10:
        text = "Looking Right"
        #keyboard.press(Key.right)
        countRight = 1
    elif x < -10:
        text = "Looking Down"
        #keyboard.press(Key.down)
        countDown = 1
    elif x > 10:
        text = "Looking Up"
        #keyboard.press(Key.up)
        countUp = 1
    else:
        text = "Forward"
        countLeft,countRight,countUp,countDown=0,0,0,0
    return [countLeft,countRight,countUp,countDown]

def click(noOfClicks):
    if noOfClicks==1:
        pyautogui.click()

    if noOfClicks==2:
        pyautogui.rightClick()

def nodeDown():   
    print("Entered function1")
    keyboard.press(Key.cmd_l)
    keyboard.press('d')
    keyboard.release('d')
    keyboard.release(Key.cmd_l)


def nodeUp():   
    print("Entered function2")  
    keyboard.press(Key.cmd_l)
    keyboard.press('d')
    keyboard.release('d')
    keyboard.release(Key.cmd_l)

def headControl(x,y,z):
    
    
    countLst=gestures(x,y,z)   
    #print(countLst)
    time.sleep(2)
    countLst1=gestures(x,y,z)
    for i in range(len(countLst)):
        countLst[i]+=countLst1[i]
    #print(countLst)
    time.sleep(2)
    countLst2=gestures(x,y,z)
    for i in range(len(countLst)):
        countLst[i]+=countLst2[i]
    #print(countLst)

    if countLst[3]==2:
        nodeDown()
    elif countLst[2]==2:
        nodeUp()
    elif countLst[2] == 3:
        keyboard.press(Key.up)
    
    elif countLst[3] == 3:
        keyboard.press(Key.down)        

    elif countLst[0] == 3:
        keyboard.press(Key.left)

    elif countLst[1] == 3:
        keyboard.press(Key.right)        
    
    countLst, countLst1, countLst2 = [0,0,0,0],[0,0,0,0],[0,0,0,0]





def inputParams(x, y, z, noOfClicks):
    scrollThread=threading.Thread(target=headControl,args=(x,y,z))
    #clickThread=threading.Thread(target=click,args=(noOfClicks))
    scrollThread.start()
    #clickThread.start()