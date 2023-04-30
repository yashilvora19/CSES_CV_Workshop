import cv2
import numpy as np








x = np.full((400,680,3), 0, dtype= 'uint8')
x[::,::] = [24,2,122]

cap = cv2.VideoCapture('VIDEOS/video.mp4')

while True:

    ret, frame = cap.read()
    x[20:380, 20:660]= frame[::,::]
    if ret == False:
        break

    cv2.imshow('win', x)
    key = cv2.waitKey(25)
    if key == ord('q'):
        break
    
cap.release()
cv2.waitKey(5000)
cv2.destroyAllWindows()


