import cv2

img=cv2.imread("shapes.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(img_gray,230,255,cv2.THRESH_BINARY_INV)

_,contours,heirarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

i=0
for cnt in contours:
	if 30000>cv2.contourArea(cnt)>200:
		M=cv2.moments(cnt)
		cx=int(M['m10']/M['m00'])
		cy=int(M['m01']/M['m00'])
		img=cv2.circle(img,(cx,cy),3,(0,0,0),-1)

		peri=cv2.arcLength(cnt,True)
		epsilon=0.01*peri
		approx=cv2.approxPolyDP(cnt,epsilon,True)
		img=cv2.drawContours(img,[approx],0,(0,255,0),3)
		x,y,w,h=cv2.boundingRect(cnt)
		if len(approx)==3:
			shape="triangle"
		elif len(approx)==4:
			_,_,theta=cv2.minAreaRect(cnt)
			if -85<theta<-5:
				shape="diamond"
			elif 0.95<w*1.0/h<1.05:
				shape="square"
			else :
				shape="rectangle"
		else :
			if 0.95<w*1.0/h<1.05:
				shape="circle"
			else:
				shape="ellipse"
		cv2.putText(img,shape,(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0))



cv2.imshow("frmae",img)
cv2.waitKey(0)
cv2.destroyAllWindows()