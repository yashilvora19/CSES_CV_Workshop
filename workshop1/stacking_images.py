import cv2
import numpy as np

img0 = cv2.imread('IMAGES/image.png')
img1 = cv2.imread('IMAGES/img2.jpg')
img2 = cv2.imread('IMAGES/img4.png')
img3 = cv2.imread('IMAGES/img5.jpeg')

print(type(img1)) # numpy array
# print(type(img))
# print(img.ndim)
# print(img.shape)

x0 =img0[0:200,0:200]
x1 =img1[0:200,0:200]
x2 =img2[0:200,0:200]
x3 =img3[0:200,0:200]

stack1 = np.hstack((x0,x1))
stack2 = np.hstack((x2,x3))

final = np.vstack((stack1, stack2))
# print(final)

cv2.imshow('python1',final)

# cv2.imshow('python2',x1)

# cv2.imshow('python3',x2)

# cv2.imshow('python4',x3)
cv2.waitKey(0)
cv2.destroyAllWindows()