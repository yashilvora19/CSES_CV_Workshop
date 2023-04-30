import numpy as np
from cv2 import cv2

# img = np.zeros((300,500,3),dtype = 'uint8')
img = cv2.imread('IMAGES/image.png')
print(img.shape)
drawing = False
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
print(img1.shape)
def draw(event,x,y,flag,params):
    global img1, drawing
    

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        # x1 = x
        # y1 = y
    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            print('hello')
            # blank =  np.copy(img)
            cv2.circle(img1, (x,y), 5, (255,0,0,0), -1)

    if event == cv2.EVENT_LBUTTONUP:
        drawing = False
       
        # rectangle = True
        # cv2.rectangle(img, (x,y), (x1,y1), (122,111,3), 2)  
cv2.namedWindow("window")
cv2.setMouseCallback("window",draw)
while True:
    cv2.imshow('window', img1)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('s'):
        cv2.imwrite('transparent.png', img1, )

cv2.destroyAllWindows()
