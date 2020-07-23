import cv2
import numpy as np

img=cv2.imread("meme.jpg",1)
rows,cols,channels=img.shape

img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

mask=cv2.inRange(img_hsv,(-5,50,70),(5,255,255))
mask_inv=cv2.bitwise_not(mask)

dst_bg=cv2.bitwise_and(img,img,mask=mask_inv)
blue=np.zeros([rows,cols,channels])
blue[:,:,0]=255*np.ones([rows,cols])
blue=blue.astype(np.uint8)

dst_fg=cv2.bitwise_and(blue,blue,mask=mask)
dst=cv2.add(dst_bg,dst_fg)

cv2.imshow('mask',mask)
cv2.imshow('result',dst)
cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()