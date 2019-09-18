import numpy as np
import cv2

img = cv2.imread('car.jpg', cv2.IMREAD_COLOR)

# COLOR ===  B G R Blue = 255,0,0  G = 0,255,0 white = 255,255,255

cv2.line(img, (0,0), (850,350), (255,0,0), 15)

cv2.rectangle(img, (15,25),(200,350),(255,255,255), 15) # 15 is line width

cv2.circle(img, (400,400), 55, (0,0,255), -1) # fill in the circle if line width is -1

cv2.circle(img, (600,800), 55, (0,0,255), 10)

# polyline and /or polygons
pts = np.array([[100,50],[200,350],[700,20],[50,10]], np.int32)

cv2.polylines(img, [pts] , True, (0,255,255),3)

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img, 'ye hi likhna h', (50,430), font, 1, (200,255,255),2,cv2.LINE_AA)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()