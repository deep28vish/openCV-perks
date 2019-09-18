import cv2
import numpy as np


# getting vid from cv2.VideoCapture 
video = cv2.VideoCapture(0)
a = 1

check, frame1 = video.read() 
check, frame2 = video.read()

while True:
    a = a +1    
        
    d = cv2.absdiff(frame1,frame2)

    grey_sc = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)    
    
    gaussian_blur = cv2.GaussianBlur(grey_sc,(3,3),0)
    
    check, th = cv2.threshold(gaussian_blur, 20, 255, cv2.THRESH_BINARY)
    
    kernel = np.ones((5,5), np.uint8)
    
    dilated = cv2.dilate(th,kernel, iterations  = 1 )
    erosion = cv2.erode(th, kernel, iterations = 1)
    
    contours, h = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.drawContours(frame1, contours, -1, (0,0,255), 2)
    
    cv2.imshow('contours', frame1)
    
#    cv2.imshow('capturing', dilated)
#    cv2.imshow('2nd', erosion)
    frame1 = frame2
    check, frame2 = video.read()    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    
print(a)
video.release

cv2.destroyAllWindows()