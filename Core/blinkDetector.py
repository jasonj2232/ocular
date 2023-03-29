import math
import time

#Function to find the Euclidean Distance between two points
def euclideanDistance(firstPoint, secondPoint):
    pointOneX, pointOneY = firstPoint
    pointTwoX, pointTwoY = secondPoint
    result = math.sqrt(((pointOneX - pointTwoX)**2) + ((pointOneY - pointTwoY)**2))
    return result * 1000

def noOfBlinks(leftEye_2d_list, rightEye_2d_list):
    flag = 0
    startTime = time.time()
    startSeconds = int(startTime % 60)

    while flag == 0:
        endTime = time.time()
        endSeconds = int(endTime % 60)
        leftEyeDist = euclideanDistance(leftEye_2d_list[0], leftEye_2d_list[1])
        rightEyeDist = euclideanDistance(rightEye_2d_list[0], rightEye_2d_list[1])
        if leftEyeDist < 1000:
            leftBlinks += 1
        if rightEyeDist < 1000:
            rightBlinks += 1
        if endSeconds - startSeconds == 3:
            break
    return tuple((leftBlinks, rightBlinks))


