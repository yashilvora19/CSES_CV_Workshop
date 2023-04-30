import cv2
import numpy as np










img = cv2.imread('../IMAGES/image.png', -1)

print(img)

print(type(img))

print(img.ndim)
print(img.shape)

x =img[0:100,0:100]

cv2.imshow('python',x)
cv2.waitKey(0)
cv2.destroyAllWindows()
