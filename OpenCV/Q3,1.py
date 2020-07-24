import cv2
import numpy as np

img=cv2.imread("dog.jpg",0)

sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelX=np.uint8(np.abs(sobelX))
sobelX=cv2.bitwise_not(sobelX)

sobelY=cv2.Sobel(img,cv2.CV_64F,0,1)
sobelY=np.uint8(np.abs(sobelY))
sobelY=cv2.bitwise_not(sobelY)

sobel=cv2.bitwise_and(sobelX,sobelY)

cv2.imshow("sobel",sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()