import cv2
import numpy as np

cap=cv2.VideoCapture("Messi.mp4")

while True:
	_,frame=cap.read()

	frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	frame_gray=cv2.medianBlur(frame_gray,9)
	circles=cv2.HoughCircles(frame_gray,cv2.HOUGH_GRADIENT,1,500,
						param1=200,param2=20,minRadius=20,maxRadius=70)
	if circles is None: 
		continue
	detected_circles=np.uint16(np.around(circles))

	for (x,y,r) in detected_circles[0,:]:
		cv2.circle(frame,(x,y),r,(0,255,0),3)

	cv2.imshow('frame',frame)

	if cv2.waitKey(40) & 0xFF==ord('q'):
		break

cap.release()



'''
#Threshold based detectors pretty often didnt detect the ball as a round object
#and hence circle shape detector most often eliminayes the ball itself.
#Hough circle detection looks to be a better alternative.

import cv2
import numpy as np

cap=cv2.VideoCapture("Messi.mp4")

while cap.isOpened():
	_,frame=cap.read()

	frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	thresh=cv2.Canny(frame_gray,100,200)
	_,thresh2=cv2.threshold(frame_gray,180,255,cv2.THRESH_BINARY)
	kernel=np.ones((5,5),dtype=np.uint8)
	thresh2=cv2.dilate(thresh2,kernel,iterations=1)
	thresh3=cv2.erode(thresh2,kernel,iterations=1)

	_,contours,heirarchy=cv2.findContours(thresh3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	for cnt in contours:
		epsilon=0.005*cv2.arcLength(cnt,True)
		approx=cv2.approxPolyDP(cnt,epsilon,True)
		(x,y,w,h)=cv2.boundingRect(approx)
		if 10000>cv2.contourArea(cnt)>1000 and len(approx)>12 :
			frame=cv2.drawContours(frame,[approx],0,(0,0,255),5)
	
	cv2.imshow("frame",frame)
	
	if cv2.waitKey(40) & 0xFF==ord('q'):
		break

cap.release()
'''