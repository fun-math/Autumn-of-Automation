import cv2
import numpy as np
import random 

img=cv2.imread("T.jpg",1)
rows,cols,ch=img.shape

M=np.float32([[1,0,0],[0,1,0]])

for i in range(8):
	x=random.randrange(40,80)
	y=random.randrange(40,80)
	sgnx=random.randrange(-1,2,2)
	sgny=random.randrange(-1,2,2)
	theta=random.randrange(0,360)
	M[0,2]=sgnx*x
	M[1,2]=sgny*y
	M_rot=cv2.getRotationMatrix2D((166,220),theta,1)
	img_new=cv2.warpAffine(img,M_rot,(cols,rows))
	img_new=cv2.warpAffine(img_new,M,(cols,rows))
	cv2.imshow(f"frame{i}",img_new)

img_blur1=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("frame8",img_blur1)

img_blur2=cv2.bilateralFilter(img,9,75,75)
cv2.imshow("frame9",img_blur2)

cv2.waitKey(0)
cv2.destroyAllWindows()