import cv2
import numpy as np 

cap=cv2.VideoCapture(0)

while True:
	_,frame=cap.read()
	frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	sobelX=cv2.Sobel(frame_gray,cv2.CV_64F,1,0)
	sobelX=np.uint8(np.abs(sobelX))
	sobelX=cv2.bitwise_not(sobelX)

	sobelY=cv2.Sobel(frame_gray,cv2.CV_64F,0,1)
	sobelY=np.uint8(np.abs(sobelY))
	sobelY=cv2.bitwise_not(sobelY)

	canny=cv2.Canny(frame_gray,50,125)
	canny=cv2.bitwise_not(canny)

	sobel=cv2.bitwise_and(sobelX,sobelY)

	cv2.imshow("sobel",sobel)
	cv2.imshow("canny",canny)

	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

cap.release()
cv2.destroyAllWindows()