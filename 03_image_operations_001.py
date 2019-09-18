import numpy as np
import cv2

img = cv2.imread('car.jpg', cv2.IMREAD_COLOR)

# reading pixel value at location 50,50
px = img[50,50]

print(px)


#replacing pixel values at location 500,500 with white pixel 255,255,255
img[500,500] = [255,255,255]

for i in range(500,520):
    for j in range(500,520):
        img[i,j] = [255,255,255]
        
# OR 
img[450:500,450:500] = [255,0,255]

# copy paste region of an image

maal = img[600:1200, 600:1200]
cv2.imshow('maal', maal)
# 1200-600 = 600
img[0:419, 0:600] = maal


# displaying the pixel which was changed above with help of circle
cv2.circle(img, (500,500), 100,(0,0,255), 10)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
