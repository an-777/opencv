import cv2
import numpy as np

# 讀取鏡頭
cap = cv2.VideoCapture(0)

if not cap.isOpened(): # 如果鏡頭沒開
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('video',frame)
    if cv2.waitKey(1) == ord('q'): # 按下 q 時結束
        break

cap.release()
cv2.destroyAllWindows()


# 讀取檔案
cap = cv2.VideoCapture('week1\image\\video.mp4')

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('video',frame)
    if cv2.waitKey(20) == ord('q'): # 按下 q 時結束
        break

cap.release()
cv2.destroyAllWindows()


# 處存影片
cap = cv2.VideoCapture(0)
 
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
 
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
 
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
 
cap.release()
out.release()
cv2.destroyAllWindows()