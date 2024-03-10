import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)


# line
cv2.line(img, (0,0), (512,512), (255,0,0), 2)
cv2.imshow('line', img)
cv2.waitKey(-1)

# rectangle
cv2.rectangle(img, (300,100), (400,200), (0,255,0), -1)
cv2.imshow('rectangle', img)
cv2.waitKey(-1)

# circle
cv2.circle(img, (100,300), 75, (0,0,255), 4)
cv2.imshow('rectangle', img)
cv2.waitKey(-1)

# ellipse
cv2.ellipse(img, (200,200), (100,50), 0, 0, 360, (255,255,0), -1)
cv2.imshow('ellipse', img)
cv2.waitKey(-1)

# polygon
pts = np.array([[10,5],[20,30],[70,40],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255))
cv2.imshow('polygon', img)
cv2.waitKey(-1)

# text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OPENCV', (10,500),  font, 4, (255,255,255), 2, cv2.LINE_AA)
cv2.imshow('text', img)
cv2.waitKey(-1)


cv2.imwrite('week1\image\drawing.jpg', img)

