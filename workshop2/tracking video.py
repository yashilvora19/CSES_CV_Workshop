import cv2
import numpy as np

img = cv2.imread('./IMAGES/blue_ball_ss_1.jpg')












hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# H = (0-179)
# S = (0-255)
# V - (0-255)
cv2.imshow('win', hsv)










def nothing(x):
    pass










cv2.namedWindow("track")

cv2.createTrackbar('H_low','track',0,179,nothing)
cv2.createTrackbar('H_high','track',0,179,nothing)
cv2.createTrackbar('S_low','track',0,255,nothing)
cv2.createTrackbar('S_high','track',0,255,nothing)
cv2.createTrackbar('V_low','track',0,255,nothing)
cv2.createTrackbar('V_high','track',0,255,nothing)













while True:
    h_l = cv2.getTrackbarPos('H_low','track')
    h_h = cv2.getTrackbarPos('H_high','track')
    s_l = cv2.getTrackbarPos('S_low','track')
    s_h = cv2.getTrackbarPos('S_high','track')
    v_l = cv2.getTrackbarPos('V_low','track')
    v_h = cv2.getTrackbarPos('V_high','track')

    low = np.array([h_l,s_l,v_l],dtype = 'uint8')
    high = np.array([h_h,s_h,v_h],dtype = 'uint8')

    mask = cv2.inRange(hsv,low,high)











    img2 = cv2.bitwise_and(img,img,mask = mask)

    cv2.imshow('win',img2)
    cv2.imshow('mask',mask)
    
    if cv2.waitKey(50) == ord('q'):
        break

cv2.destroyAllWindows()
