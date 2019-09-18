import numpy as np
import cv2

cap = cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
    
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 3)
    
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 3)
    
    edges = cv2.Canny(frame, 100,100)
    
    
    cv2.imshow('orig', frame)
    
    cv2.imshow('edges', edges)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    


cv2.destroyAllWindows()
cap.release()