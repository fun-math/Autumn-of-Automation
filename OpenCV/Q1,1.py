import cv2 

img=cv2.imread("dog.jpg",1)

dog_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('dog',dog_grey)
cv2.waitKey(0)
cv2.destroyAllWindows()