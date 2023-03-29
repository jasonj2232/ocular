# import cv2 as cv 
# import numpy as np
# import mediapipe as mp 
# mp_face_mesh = mp.solutions.face_mesh

# # left eyes indices
LEFT_EYE =[ 362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385,384, 398 ]
# # right eyes indices
# RIGHT_EYE=[ 33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246 ] 

# # irises Indices list
# LEFT_IRIS = [474,475, 476, 477]
# RIGHT_IRIS = [469, 470, 471, 472]

# cap = cv.VideoCapture(0)

# with mp_face_mesh.FaceMesh(
#     max_num_faces=1,
#     refine_landmarks=True,
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5
# ) as face_mesh:

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         frame = cv.flip(frame, 1)

#         rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
#         img_h, img_w = frame.shape[:2]
#         results = face_mesh.process(rgb_frame)
#         mask = np.zeros((img_h, img_w), dtype=np.uint8)

#         if results.multi_face_landmarks:
#             # print((results.multi_face_landmarks[0]))

#             # [print(p.x, p.y, p.z ) for p in results.multi_face_landmarks[0].landmark]
            
#             mesh_points=np.array([np.multiply([p.x, p.y], [img_w, img_h]).astype(int) 
#             for p in results.multi_face_landmarks[0].landmark])

#             # cv.polylines(frame, [mesh_points[LEFT_IRIS]], True, (0,255,0), 1, cv.LINE_AA)
#             # cv.polylines(frame, [mesh_points[RIGHT_IRIS]], True, (0,255,0), 1, cv.LINE_AA)
            
#             (l_cx, l_cy), l_radius = cv.minEnclosingCircle(mesh_points[LEFT_IRIS])
#             (r_cx, r_cy), r_radius = cv.minEnclosingCircle(mesh_points[RIGHT_IRIS])
#             center_left = np.array([l_cx, l_cy], dtype=np.int32)
#             center_right = np.array([r_cx, r_cy], dtype=np.int32)
#             cv.circle(frame, center_left, int(l_radius), (0,255,0), 2, cv.LINE_AA)
#             cv.circle(frame, center_right, int(r_radius), (0,255,0), 2, cv.LINE_AA)

#             # cv.circle(frame, center_left, 1, (0,255,0), -1, cv.LINE_AA)
#             # cv.circle(frame, center_right, 1, (0,255,0), -1, cv.LINE_AA)

#             # drawing on the mask 
#             cv.circle(mask, center_left, int(l_radius), (255,255,255), -1, cv.LINE_AA)
#             cv.circle(mask, center_right, int(r_radius), (255,255,255), -1, cv.LINE_AA)
            
#         cv.imshow('Mask', mask)     
#         cv.imshow('img', frame)
#         key = cv.waitKey(1)
#         if key ==ord('q'):
#             break
# cap.release()
# cv.destroyAllWindows()

#import all the necessary libraries.
import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark

        for i in 
        
        for id, landmark in enumerate(landmarks[LEFT_EYE]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)


