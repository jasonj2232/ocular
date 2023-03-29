import cv2
import mediapipe as mp
import numpy as np
import time
import math
from pynput.keyboard import Key, Controller
import gesture as ges


#Function to find the Euclidean Distance between two points
def euclideanDistance(firstPoint, secondPoint):
    pointOneX, pointOneY = firstPoint
    pointTwoX, pointTwoY = secondPoint
    result = math.sqrt(((pointOneX - pointTwoX)**2) + ((pointOneY - pointTwoY)**2))
    return result

# Last 4 values in the array are eye related
# Left Eye top = 386; Left Eye bot = 374; Right Eye top = 159; Right Eye bot = 145
interestedLandmarks = [33, 263, 1, 61, 291, 199, 159, 145, 386, 374] 
leftEye = [386, 374]
rightEye = [159, 145]

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

# keypress module intializatons
keyboard = Controller()

cap = cv2.VideoCapture(0)

count_down=0
count_up=0

while cap.isOpened():
    success, image = cap.read()

    start = time.time()

    # Flip the image horizontally for a later selfie-view display
    # Also convert the color space from BGR to RGB
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

    # To improve performance
    image.flags.writeable = False
    
    # Get the result
    results = face_mesh.process(image)
    
    # To improve performance
    image.flags.writeable = True
    
    # Convert the color space from RGB to BGR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    img_h, img_w, img_c = image.shape
    face_3d = []
    face_2d = []
    rightEye_2d_list = []
    leftEye_2d_list = []

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            for idx, lm in enumerate(face_landmarks.landmark):
                if idx in interestedLandmarks:
                    if idx == 1:
                        nose_2d = (lm.x * img_w, lm.y * img_h)
                        nose_3d = (lm.x * img_w, lm.y * img_h, lm.z * 3000)
                    
                    if idx == 159 or idx == 145:
                        rightEye_2d = (lm.x * img_w, lm.y * img_h)
                        rightEye_2d_list.append(rightEye_2d)
                        #rightEye_3d = (lm.x * img_w, lm.y * img_h, lm.z * 3000)

                    if idx == 386 or idx == 374:
                        leftEye_2d = (lm.x * img_w, lm.y * img_h)
                        leftEye_2d_list.append(leftEye_2d)
                        #leftEye_3d = (lm.x * img_w, lm.y * img_h, lm.z * 3000)

                    x, y = int(lm.x * img_w), int(lm.y * img_h)

                    # Get the 2D Coordinates
                    face_2d.append([x, y])

                    # Get the 3D Coordinates
                    face_3d.append([x, y, lm.z])       
            
            # Convert it to the NumPy array
            face_2d = np.array(face_2d, dtype=np.float64)

            # Convert it to the NumPy array
            face_3d = np.array(face_3d, dtype=np.float64)

            # The camera matrix
            focal_length = 1 * img_w

            cam_matrix = np.array([ [focal_length, 0, img_h / 2],
                                    [0, focal_length, img_w / 2],
                                    [0, 0, 1]])

            # The distortion parameters
            dist_matrix = np.zeros((4, 1), dtype=np.float64)

            # Solve PnP
            success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)

            # Get rotational matrix
            rmat, jac = cv2.Rodrigues(rot_vec)

            # Get angles
            angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)

            # Get the y rotation degree
            x = angles[0] * 360
            y = angles[1] * 360
            z = angles[2] * 360
            
            rightEyeDist = euclideanDistance(rightEye_2d_list[0], rightEye_2d_list[1])
            leftEyeDist = euclideanDistance(leftEye_2d_list[0], leftEye_2d_list[1])

            print(rightEyeDist)
            print(leftEyeDist)

            if leftEyeDist < 5:
                keyboard.press(Key.left)
            
            if rightEyeDist < 5:
                keyboard.press(Key.right)

            # See where the user's head tilting
            
            if y < -10:
                text = "Looking Left"
                keyboard.press(Key.left)
            elif y > 10:
                text = "Looking Right"
                keyboard.press(Key.right)
            elif x < -10:
                text = "Looking Down"
                # keyboard.press(Key.down)
                count_down+=1                
                ges.node_down(count_down)
                time.sleep(1)
            elif x > 10:
                text = "Looking Up"
                # keyboard.press(Key.up)
                count_up+=1                
                ges.node_up(count_up)
                time.sleep(1)
            else:
                text = "Forward"

            

            # Display the nose direction
            # nose_3d_projection, jacobian = cv2.projectPoints(nose_3d, rot_vec, trans_vec, cam_matrix, dist_matrix)

            # p1 = (int(nose_2d[0]), int(nose_2d[1]))
            # p2 = (int(nose_2d[0] + y * 10) , int(nose_2d[1] - x * 10))
            
            # cv2.line(image, p1, p2, (255, 0, 0), 3)

            # # Add the text on the image
            # cv2.putText(image, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
            # cv2.putText(image, "x: " + str(np.round(x,2)), (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            # cv2.putText(image, "y: " + str(np.round(y,2)), (500, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            # cv2.putText(image, "z: " + str(np.round(z,2)), (500, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


        end = time.time()
        totalTime = end - start

        fps = 1 / totalTime
        #print("FPS: ", fps)

        cv2.putText(image, f'FPS: {int(fps)}', (20,450), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)

        mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=drawing_spec,
                    connection_drawing_spec=drawing_spec)


    cv2.imshow('Head Pose Estimation', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break


cap.release()