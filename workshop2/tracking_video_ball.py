import cv2
import numpy as np

x = cv2.VideoCapture('./VIDEOS/blue_ball.mp4')

while True:
    low = np.array([94, 98, 95],dtype = 'uint8')
    high = np.array([117, 255, 255],dtype = 'uint8')
    ret, frame = x.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)



    mask = cv2.inRange(hsv,low,high)
    new_mask = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow('og' , frame)
    cv2.imshow('win' , mask)
    cv2.imshow('win2', new_mask)
    if cv2.waitKey(35)== ord('q'):
        break



x.release()
cv2.destroyAllWindows()