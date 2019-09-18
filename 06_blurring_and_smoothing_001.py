import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# how to find hsv value to track?

# 1st find your color in BGR format suppose its green 0,255,0
green = np.uint8([[[0,255,0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(hsv_green)
# [[[ 60 255 255]]]
# Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively
# lower_green = np.array([50,100,100])
#    upper_green = np.array([70,255,255])

limit = hsv_green[0][0][0]
ll = limit - 10
ul = limit + 10
while True:
    _, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # hsv = hue , sat, value
    lower_red = np.array([ll,100,100])
    upper_red = np.array([ul,255,255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    kernel = np.ones((15,15), np.float32) / 225
    
    smoothed = cv2.filter2D(res, -1, kernel)
    
    blur = cv2.GaussianBlur(res, (15,15), 0)
    
#    cv2.imshow('frame', frame)
#    cv2.imshow('mask', mask)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    


cv2.destroyAllWindows()
cap.release()