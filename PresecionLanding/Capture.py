import cv2
import numpy as np
import time
import imutils as im

cap = cv2.VideoCapture(0)

name = "outImg"
i = 0

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	cv2.imshow('Frame',frame)
	key = cv2.waitKey(1) & 0xFF ;
	
	if key == ord("c"):
		new = name + str(i) + ".jpg"
		print new
		i = i+1
		cv2.imwrite(new,frame)

	if key == ord("q"):
		break

cv2.destroyAllWindows()