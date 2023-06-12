import cv2
import numpy as np
# Variables
R = 0
G = 0
B = 0
# callback function for RED slider
def redValue(value):
    global R # changes in red trackbar position updates "value" which is copied to R
    R = value
def greenValue(value):
    global G # changes in green trackbar position updates "value" which is copied to G
    G = value
def blueValue(value):
    global B # changes in blue trackbar position updates "value" which is copied to B
    B = value
# Creating a black image/frame (0 pixel value) of 500x500 size
frame = np.zeros((500,500,3), np.uint8)
# Creating an window for trackbars and frame
cv2.namedWindow('FRAME')
cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars',500,130)
# Creating three different trackbars for RGB channels
cv2.createTrackbar('RED','Trackbars',R,255,redValue)
cv2.createTrackbar('GREEN','Trackbars',G,255,greenValue)
cv2.createTrackbar('BLUE','Trackbars',B,255,blueValue)
while True:
    frame[:,:,2] = R
    frame[:,:,1] = G
    frame[:,:,0] = B
    cv2.imshow('FRAME',frame)
    if cv2.waitKey(1) & 0xff == ord('q'): # to quit press 'q'
        break
cv2.destroyAllWindows()