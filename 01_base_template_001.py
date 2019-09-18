import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('car.jpg',cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread('car.jpg', cv2.IMREAD_COLOR) # BGR FORMAT
img2 = cv2.imread('car.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('img any name', img)

cv2.imshow('img any name 1', img1)

cv2.imshow('img any name 2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
# open image via matplotlib is RGB
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.plot([50,100],[180,100],'c',linewidth = 5)
plt.show
# saving image 
cv2.imwrite('car_gray.png',img)

# getting vid from cv2.VideoCapture 

video = cv2.VideoCapture(0)

a = 1

# saving video 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0,(640,480))

while True:
    a = a +1    
        
    check, frame = video.read()
    cv2.imshow('Feed',frame )
    
    
    # saving video 
    out.write(frame)
        
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    
print(a)
video.release()
out.release()

cv2.destroyAllWindows()