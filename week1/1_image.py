import cv2
import numpy as np


# 讀取圖片
img = cv2.imread('week1\image\img.jpg')
# 顯示圖片
cv2.imshow('img', img)
# 處存圖片
blackImg = np.zeros((512,512,3))
cv2.imshow('blackImg', blackImg)
cv2.imwrite('week1\image\write.jpg', blackImg)


cv2.waitKey(0)
cv2.destroyAllWindows()