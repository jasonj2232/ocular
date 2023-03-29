import cv2
import numpy as np

def tracking(img_w, img_h, face_2d, face_3d):
    # The camera matrix
    focal_length = 1 * img_w
    
    cam_matrix = np.array([[focal_length, 0, img_h / 2],[0, focal_length, img_w / 2],[0, 0, 1]])

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

    return x, y, z