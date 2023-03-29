import math
import time

#Function to find the Euclidean Distance between two points
def euclideanDistance(firstPoint, secondPoint):
    pointOneX, pointOneY = firstPoint
    pointTwoX, pointTwoY = secondPoint
    result = math.sqrt(((pointOneX - pointTwoX)**2) + ((pointOneY - pointTwoY)**2))
    return result

def noOfBlinks(leftEye_2d_list, rightEye_2d_list):
    totalTime, leftBlinks, rightBlinks = 3, 0, 0
    while totalTime != 0:
        leftEyeDist = euclideanDistance(leftEye_2d_list[0], leftEye_2d_list[1])
        rightEyeDist = euclideanDistance(rightEye_2d_list[0], rightEye_2d_list[1])
        if leftEyeDist < 7:
            leftBlinks += 1
        if rightEyeDist < 7:
            rightBlinks += 1
        time.sleep(1)
        totalTime -= 1
    return tuple((leftBlinks, rightBlinks))

