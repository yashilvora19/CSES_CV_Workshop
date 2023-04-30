import numpy as np
import cv2

img = np.zeros((450,450,3), dtype='uint8')
drawing = False

cv2.namedWindow("win")

def nothing(x):
    pass

cv2.createTrackbar('R', 'win', 0, 255, nothing)
cv2.createTrackbar('G', 'win', 0, 255, nothing)
cv2.createTrackbar('B', 'win', 0, 255, nothing)

def paintbrush(event,x,y,flag,params):
    global drawing, img,r,g,b
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img, (x,y), 10, (b,g,r), -1)
    if event == cv2.EVENT_LBUTTONUP:
        drawing = False


cv2.setMouseCallback("win", paintbrush)

while True:
    r = cv2.getTrackbarPos('R', 'win')
    g = cv2.getTrackbarPos('G', 'win')
    b = cv2.getTrackbarPos('B', 'win')
    cv2.imshow("win", img)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()


