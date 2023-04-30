import numpy as np
from cv2 import cv2
# dtype = 'uint8'


img = np.zeros((300,500,3),dtype = 'uint8')


def nothing(x):
    pass

cv2.namedWindow("image")


cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
while True:
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')

    img[::] = [b,g,r]

    cv2.imshow("image",img)
    if cv2.waitKey(100) == ord('q'):
        break

cv2.destroyAllWindows()


