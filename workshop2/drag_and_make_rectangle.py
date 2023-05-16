import numpy as np
import cv2

# Opening the image
img = cv2.imread('./IMAGES/sample1.jpg')

drawing = False
x1 = 0
y1 = 0
blank =  np.copy(img)
x2= 0
y2= 0

# mouse callback function

def draw(event,x,y,flag,params):
    global img,drawing,x1,y1, blank, x2, y2, rectangle

    # 3 different events of pressing and holding the left button of the mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x1 = x
        y1 = y
    
    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            blank =  np.copy(img)
            cv2.rectangle(blank, (x,y), (x1,y1), (0,0,255), 5)

    if event == cv2.EVENT_LBUTTONUP:
        drawing = False
        x2 = x
        y2 = y

# Creating a window and setting the mouse callback to that window while calling 
# the draw function

cv2.namedWindow("window")
cv2.setMouseCallback("window",draw)
a = np.copy(img)

# While loop to detect the x,y coordinates and drawing the rectangle
while True:    
    cv2.imshow("window",blank)
    key = cv2.waitKey(50)
    if key ==ord('q'):
        break
cv2.destroyAllWindows()
