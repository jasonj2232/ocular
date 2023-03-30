import math
import time

#Function to find the Euclidean Distance between two points
def euclideanDistance(firstPoint, secondPoint):
    pointOneX, pointOneY = firstPoint
    pointTwoX, pointTwoY = secondPoint
    result = int(math.sqrt(((pointOneX - pointTwoX)**2) + ((pointOneY - pointTwoY)**2)))
    return result * 100

def noOfBlinks(leftEye_2d_list, rightEye_2d_list):
    flag, leftBlinks, rightBlinks, totalBlink, actualBlink = 0, 0, 0, 0, 0
    flag1, flag2, flag3 = 0, 0, 0
    startTime = time.time()
    startSeconds = int(startTime % 60)
    #print(time.ctime(startTime))
    while flag == 0:
        endTime = time.time()
        endSeconds = int(endTime % 60)
        leftEyeDist = euclideanDistance(leftEye_2d_list[0], leftEye_2d_list[1])
        rightEyeDist = euclideanDistance(rightEye_2d_list[0], rightEye_2d_list[1])
        #print("Left Eye Dist\t", leftEyeDist)
        #print("Right Eye Dist\t", rightEyeDist)
        if leftEyeDist < 800:
            leftBlinks += 1
            #print("Blink Detected")
        if rightEyeDist < 800:
            rightBlinks += 1
        if endSeconds - startSeconds == 1 and flag1 == 0:
            totalBlink += leftBlinks
            flag1 = 1
            print("total1\t", totalBlink)
        if endSeconds - startSeconds == 2 and flag2 == 0:
            totalBlink += leftBlinks
            flag2 = 1
            print("total2\t", totalBlink)
        if endSeconds - startSeconds == 3:
            #print("broken")
            flag1 = 0
            flag2 = 0
            print(flag1)
            actualBlink = int(totalBlink / 850000)
            print(actualBlink)
            actualBlink -= 1
            print("actual\t", actualBlink)
            #print("left\t", totalBlink)
            break
    #print(time.ctime(endTime))
    return tuple((actualBlink, actualBlink))


