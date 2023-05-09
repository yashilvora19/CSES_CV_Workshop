import numpy as np
import cv2

img = cv2.imread('./IMAGES/sample1.jpg')

drawing = False
x1 = 0
y1 = 0
blank =  np.copy(img)
x2= 0
y2= 0

# mouse callback function
rectangle = False
saved = False


def draw(event,x,y,flag,params):
    global img,drawing,x1,y1, blank, x2, y2, rectangle

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x1 = x
        y1 = y
    
    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            blank =  np.copy(img)
            # if x1>x and y1>y:
            cv2.rectangle(blank, (x,y), (x1,y1), (0,0,255), 5)

    if event == cv2.EVENT_LBUTTONUP:
        drawing = False
        x2 = x
        y2 = y
        rectangle = True

cv2.namedWindow("window")
cv2.setMouseCallback("window",draw)
a = np.copy(img)

while True:    
    cv2.imshow("window",blank)
    key = cv2.waitKey(50)
    if key ==ord('q'):
        break
    if key == ord('c') and rectangle == True:
        
        if rectangle == True:
            if x1>x2 and y1>y2:
                crop = img[y2:y1, x2:x1]
            cv2.imshow("crop", crop)
            saved = True
        else:
            print('MAKE THE RECTANGLE FIRST')
    if key == ord('s') and saved == True:
        if saved == True:
            cv2.imwrite('./IMAGES/crop.jpg', crop)
        else:
            print('CROP IMAGE FIRST')
cv2.destroyAllWindows()
