#None of Flann based or brute force method gave good
# resutls.

  
import cv2
import numpy as np 

cap=cv2.VideoCapture("Messi.mp4")
_,_=cap.read()
_,_=cap.read()
_,_=cap.read()
_,_=cap.read()

template=cv2.imread("whiteball.jpeg",0)
_,template=cv2.threshold(template,100,255,cv2.THRESH_TOZERO)
#template=cv2.bitwise_not(template)
orb=cv2.ORB_create()

while cap.isOpened():
	_,frame=cap.read()

	frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	frame_gray=frame_gray.astype(np.uint8)
	mask=np.zeros([720,1280],dtype=np.uint8)
	mask[100:200,0:250]=(255*np.ones([100,250])).astype(np.uint8)
	mask=cv2.bitwise_not(mask)
	frame_gray=cv2.bitwise_and(frame_gray,frame_gray,mask=mask)
	kp1,des1=orb.detectAndCompute(template,None)
	kp2,des2=orb.detectAndCompute(frame_gray,None)
	

	if  des1 is None or des2 is None:
		continue

	des1=des1.astype(np.float32)
	des2=des2.astype(np.float32)

	FLANN_INDEX_KDTREE = 0
	index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
	search_params = dict()

	flann=cv2.FlannBasedMatcher(index_params,search_params)
	matches=flann.knnMatch(des1,des2,k=2)

	matchesMask=[[0,0] for i in xrange(len(matches))]

	for i,(m,n) in enumerate(matches):
	   	if m.distance < 0.8*n.distance:
	   		matchesMask[i]=[1,0]

	draw_params = dict(matchColor = (0,0,255),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = 0)
	img = cv2.drawMatchesKnn(template,kp1,frame,kp2,matches,None,**draw_params)
	#cv2.imshow('mask',mask)
	cv2.imshow("frame",img)
	if cv2.waitKey(40) & 0xFF==ord('q'):
		break
print(frame_gray.shape)
cap.release()



'''
#Brute force approach


import cv2
import numpy as np

cap=cv2.VideoCapture("Messi.mp4")
_,_=cap.read()
_,_=cap.read()
_,_=cap.read()
_,_=cap.read()

template=cv2.imread("football.png",0)
orb=cv2.ORB_create()
bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

while cap.isOpened():
	_,frame=cap.read()

	frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	frame_gray=frame_gray.astype(np.uint8)
	kp1,des1=orb.detectAndCompute(template,None)
	kp2,des2=orb.detectAndCompute(frame_gray,None)

	if  des1 is None or des2 is None:
		continue

	matches=bf.match(des1,des2)
	matches=sorted(matches, key=lambda x:x.distance)
	img=cv2.drawMatches(template,kp1,frame,kp2,matches[0:100],None,flags=2)
	cv2.imshow('frame',img)


	if cv2.waitKey(40) & 0xFF==ord('q'):
		break
print(frame_gray.shape)
print(template.shape)
print(des1.shape)
print(des2.shape)

cap.release()
'''