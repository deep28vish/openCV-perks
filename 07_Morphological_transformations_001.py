import numpy as np
import cv2

cap = cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # hsv = hue , sat, value
    lower_red = np.array([50,100,100])
    upper_red = np.array([70,255,255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 1)
    
    dilation = cv2.erode(mask, kernel, iterations = 1)
    
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN ,kernel)
    
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE ,kernel)
            
    cv2.imshow('frame', frame)
#    cv2.imshow('mask', mask)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)
    
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    


cv2.destroyAllWindows()
cap.release()