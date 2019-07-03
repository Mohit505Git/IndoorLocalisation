# Checks if a matrix is a valid rotation matrix.
def isRotationMatrix(R) :
    Rt = np.transpose(R)
    shouldBeIdentity = np.dot(Rt, R)
    I = np.identity(3, dtype = R.dtype)
    n = np.linalg.norm(I - shouldBeIdentity)
    return n < 1e-6
 
 
# Calculates rotation matrix to euler angles
# The result is the same as MATLAB except the order
# of the euler angles ( x and z are swapped ).
def rotationMatrixToEulerAngles(R) :
 
    assert(isRotationMatrix(R))
     
    sy = np.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
     
    singular = sy < 1e-6
 
    if  not singular :
        x = np.arctan2(R[2,1] , R[2,2])
        y = np.arctan2(-R[2,0], sy)
        z = np.arctan2(R[1,0], R[0,0])
    else :
        x = np.arctan2(-R[1,2], R[1,1])
        y = np.arctan2(-R[2,0], sy)
        z = 0
 
    return np.array([x, y, z])

import apriltag
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	detector = apriltag.Detector()
	result = detector.detect(gray)
    
	K = np.array([[6.331284731799049723e+02,0.000000000000000000e+00,3.240546706735938187e+02],[0.000000000000000000e+00,6.276117931324869232e+02,2.404437048001034611e+02],[0.000000000000000000e+00,0.000000000000000000e+00,1.000000000000000000e+00]])
	K_inv = np.linalg.inv(K)

	
	if len(result) != 0:
		center = result[0].center
		H = np.array(result[0].homography)
		# print H
		h1h2h3 = np.dot(K_inv,H)

		h1T = h1h2h3[:,0]
		h2T = h1h2h3[:,1]
		h3T = h1h2h3[:,2]
		
		h1Xh2T = np.cross(h1T,h2T)

		print "h1Xh2T",h1Xh2T
		h1_h2_h1Xh2T = np.array([h1T,h2T,h1Xh2T])
		h1_h2_h1Xh2 = np.transpose(h1_h2_h1Xh2T)

		u, s, vh = np.linalg.svd(h1_h2_h1Xh2, full_matrices=True)

		uvh = np.dot(u,vh)
		det_OF_uvh = np.linalg.det(uvh)

		M = np.array([[1,0,0],[0,1,0],[0,0,det_OF_uvh]])

		r = np.dot(u,M)
		R = np.dot(r,vh)

		T = h3T/np.linalg.norm(h1T)

		if T[2] < 0:
			flag = -1
		else : 
			flag = 1

		mat = rotationMatrixToEulerAngles(R*flag)

		roll = mat[0]
		pitch =  mat[1]
		yaw = mat[2]

		print "Translation",T*flag
		print "roll",roll,"pitch",pitch,"yaw",yaw

	# Display the resulting frame
	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()