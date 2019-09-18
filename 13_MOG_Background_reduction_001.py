import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    
    ret, frame = cap.read()
    
    fgmask = fgbg.apply(frame)
    
    cv2.imshow('orig',frame)
    cv2.imshow('fg', fgmask)
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    

cap.release()

cv2.destroyAllWindows()