import cv2
import numpy as np
# Using VideoCapture to read the video
x = cv2.VideoCapture('./VIDEOS/blue_ball.mp4')

while True:
    # We got these values from the tracking_ball_masking.py file
    low = np.array([94, 98, 95],dtype = 'uint8')
    high = np.array([117, 255, 255],dtype = 'uint8')
    # Reading the video frame by frame
    ret, frame = x.read()
    # Converting every frame from BGR to HSV format
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # Creating mask for every frame and displaying it to a window 
    mask = cv2.inRange(hsv,low,high)
    new_mask = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow('og' , frame)
    cv2.imshow('win' , mask)
    cv2.imshow('win2', new_mask)
    # Quitting key
    if cv2.waitKey(35)== ord('q'):
        break

x.release()
cv2.destroyAllWindows()