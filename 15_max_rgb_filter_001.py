# MAX RGB FILTER
# any pixel which have high intensity of any particular color will be intensified and rest all will be over shadowed
# pixcel per pexcel basis

import cv2
import numpy as np
# getting vid from cv2.VideoCapture 
video = cv2.VideoCapture(0)
a = 1

while True:
    a = a +1    
    
    check, frame = video.read() 
    
    (B,G,R) = cv2.split(frame)
    
    M = np.maximum(np.maximum(R, G),B)
    
    R[R<M] = 0
    G[G<M] = 0
    B[B<M] = 0

    frame1 = cv2.merge((B,G,R))    
    
    cv2.imshow('capturing', frame1)
        
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    
print(a)
video.release

cv2.destroyAllWindows()