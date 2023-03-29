import cv2
import mediapipe as mp
import numpy as np
#import time
import math
import gesture
import head

#Initialising required objects
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
#mp_drawing = mp.solutions.drawing_utils
#drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
keyboard = Controller()

cap = cv2.VideoCapture(0)

#Mediapipe Facemesh points
interestedLandmarks = [33, 263, 1, 61, 291, 199, 159, 145, 386, 374] 
leftEye = [386, 374]
rightEye = [159, 145]

while cap.isOpened():
    success, image = cap.read()

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

            x, y, z = head.tracking(img_w, img_h, face_2d, face_3d)

            gesture.gestures(x, y, z)
    
    if cv2.waitKey(5) & 0xFF == 27:
        break
    
cap.release()