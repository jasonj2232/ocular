import math
import time

#Function to find the Euclidean Distance between two points
def euclideanDistance(firstPoint, secondPoint):
    pointOneX, pointOneY = firstPoint
    pointTwoX, pointTwoY = secondPoint
    result = int(math.sqrt(((pointOneX - pointTwoX)**2) + ((pointOneY - pointTwoY)**2)))
    return result*100

def noOfBlinks(leftEye_2d_list, rightEye_2d_list):
    totalTime, leftBlinks, rightBlinks = 3, 0, 0
    timeatbeg = time.time()
    ctb=time.ctime(timeatbeg)
    tb=int(ctb.split(" ")[3].split(":")[2])
    print(tb)
    while totalTime > 2.99:        
        
        leftEyeDist = euclideanDistance(leftEye_2d_list[0], leftEye_2d_list[1])
        # print("Left Eye Dist\t", leftEyeDist)
        rightEyeDist = euclideanDistance(rightEye_2d_list[0], rightEye_2d_list[1])
        # print("Right Eye Dist\t", rightEyeDist)
        if leftEyeDist < 12:
            leftBlinks += 1
            
        if rightEyeDist < 12:
            rightBlinks += 1
            
        timeatend = time.time()
        cte=time.ctime(timeatend)
        te=int(cte.split(" ")[3].split(":")[2])
        if te-tb ==3:
            print("diff",timeatend-timeatbeg)
            break
        
        print(leftBlinks,rightBlinks)

        
        

        

        
        # print(totalTime)
        # time.sleep(1)
        totalTime += time.time()
    return tuple((leftBlinks, rightBlinks))

