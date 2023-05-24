import cv2
import numpy as np


# Getting your laptop's camera capture (0 should be the argument)
cap = cv2.VideoCapture(0)

# Making 2 kernels for erosion and dilation
kernel1 = np.ones((5,5),dtype = 'uint8')
kernel2 = np.ones((3,3),dtype = 'uint8')

l = []

# Boolean variable which decides whether to start painting or not
paint = False

# While loop for editing the video frame by frame 
while True:
    key = cv2.waitKey(1)
    # Setting paint to true if p is pressed on the keyboard
    if key == ord('p'): 
        paint = True          

    ret, frame = cap.read()
    
    # Making the frame a mirror image
    frame = cv2.flip(frame, 1)
    # Converting to HSV to create a mask and filter out the color (blue, in this case)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Creating the mask
    low = np.array([95,160,121],dtype = 'uint8')
    high = np.array([121,255,255],dtype = 'uint8')

    mask = cv2.inRange(hsv,low,high)

    '''
    Getting a better mask. These are morphological operators commonly used in 
    image processing. These operations are often used for tasks like noise 
    removal, image enhancement, and object detection.


    cv2.erode()
    The cv2.erode() function is used for erosion, which is a morphological 
    operation that shrinks or erodes the boundaries of foreground objects in 
    an image. It achieves this by moving a structuring element over the image 
    and replacing the pixel at the center of the structuring element with the 
    minimum pixel value within the neighborhood.

    SYNTAX: 
    cv2.erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])


    cv2.dilate()
    The cv2.dilate() function is used for dilation, which is the opposite of 
    erosion. It expands or thickens the boundaries of foreground objects in an 
    image. It achieves this by moving a structuring element over the image and 
    replacing the pixel at the center of the structuring element with the 
    maximum pixel value within the neighborhood.

    SYNTAX:
    cv2.dilate(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])

    '''
    erode = cv2.erode(mask, kernel1, iterations= 1)
    dilate = cv2.dilate(erode, kernel1, iterations= 1)
    dilate = cv2.dilate(dilate, kernel2, iterations= 3)
    
    # No value to our code- used for visualizing the mask
    # img2 = cv2.bitwise_and(frame, frame,mask = dilate)

    '''
    The cv2.findContours() function is a method provided by the OpenCV library 
    for contour detection in images. Contours are simply the boundaries of 
    objects or shapes in an image. The cv2.findContours() function takes a 
    binary image as input and returns a list of contours found in that image.

    SYNTAX:
    contours, hierarchy = cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]])

    '''
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if len(contours)>0:
        # Making a rectangle around the pointer
        x,y,h,w = cv2.boundingRect(contours[0])
        x1= int(x+h/2+20)
        y1= int(y+(w/2))
        cv2.circle(frame, (x1, y1), 15, (0,0,255), -1)
        if paint:        
            l.append((x1,y1))
        
    else:
        pass

    # If paint is true, drawing on the captured frame
    if paint:       
        for x2,y2 in l:
            # Try changing the color of the circle!
            cv2.circle(frame, (x2,y2), 5, (105,105,105), -1)
        # Connecting lines between the circles
        if len(l)>1:
            for i in range(1, len(l)):
                cv2.line(frame, (l[i-1][0], l[i-1][1]),(l[i][0], l[i][1]), (200,127,75), 5)

    # Displaying output
    cv2.imshow('window',frame)

    # cv2.imshow('win',img2)
    # cv2.imshow('mask',dilate)
    
    # Exit key for program
    if key == ord('q'):
        break
# Releasing and destroying all windows
cap.release()
cv2.waitKey(3000)
cv2.destroyAllWindows()

