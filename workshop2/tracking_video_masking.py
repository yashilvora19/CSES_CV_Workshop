import cv2
import numpy as np

img = cv2.imread('./IMAGES/blue_ball_ss_1.jpg')

# Converting to HSV
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# H = (0-179)
# S = (0-255)
# V - (0-255)
cv2.imshow('win', hsv)

# Nothing function to pass into the createTrackbar function
def nothing(x):
    pass

cv2.namedWindow("track")

# Creating the six trackbars for the high and lows values of H(ue), S(aturation) and V(alue)
cv2.createTrackbar('H_low','track',0,179,nothing)
cv2.createTrackbar('H_high','track',0,179,nothing)
cv2.createTrackbar('S_low','track',0,255,nothing)
cv2.createTrackbar('S_high','track',0,255,nothing)
cv2.createTrackbar('V_low','track',0,255,nothing)
cv2.createTrackbar('V_high','track',0,255,nothing)

# Getting trackbar position in the while loop
while True:
    h_l = cv2.getTrackbarPos('H_low','track')
    h_h = cv2.getTrackbarPos('H_high','track')
    s_l = cv2.getTrackbarPos('S_low','track')
    s_h = cv2.getTrackbarPos('S_high','track')
    v_l = cv2.getTrackbarPos('V_low','track')
    v_h = cv2.getTrackbarPos('V_high','track')

    # Storing the high and low values in 2 different arrays
    low = np.array([h_l,s_l,v_l],dtype = 'uint8')
    high = np.array([h_h,s_h,v_h],dtype = 'uint8')

    # Using inRnage function to make a mask- read up about this online 
    mask = cv2.inRange(hsv,low,high)

    # Using bitwise and operation to combine the mask with the image and getting the desired output
    img2 = cv2.bitwise_and(img,img,mask = mask)

    cv2.imshow('win',img2)
    cv2.imshow('mask',mask)
    
    if cv2.waitKey(50) == ord('q'):
        break

cv2.destroyAllWindows()
