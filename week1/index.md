# Week 1 - Gui Features in OpenCV

## 圖片

- 讀取圖片: `cv.imread(filename[, flags])`
  - flags: 
    - cv2.IMREAD_COLOR: `1`
    - cv2.IMREAD_GRAYSCALE: `0`
    - cv2.IMREAD_UNCHANGED: `-1`
- 顯示圖片: `cv.imshow(winname, mat)`
- 寫入圖片: `cv.imwrite(filename, img)`
- 等待: `cv2.waitKey()`
  - 毫秒, `0` 表示無限
- 關閉所有視窗: `cv2.destroyAllWindows()`

```python
import cv2
import numpy as np

# 讀取圖片
img = cv2.imread('week1\\img.jpg')
# 顯示圖片
cv2.imshow('img', img)
# 寫入圖片
blackImg = np.zeros((512,512,3)) # 一張黑色圖片(512*512px)
cv2.imshow('blackImg', blackImg)
cv2.imwrite('week1\\write.jpg', blackImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
```
## 影片

- 讀取影片
  - 從鏡頭讀取: `cv2.VideoCapture(index)`
    - 從 index 從 0 開始
  - 從檔案讀取: `cv2.VideoCapture(filename)`
- 播放影片: `ret, frame = cap.read()` 
  ```python
  while True:
      ret, frame = cap.read()

      if not ret:
          break

      cv2.imshow('video',frame)
  ```
- 釋放資源: `cap.release()`
- 寫入影片
  - 設定 fourcc: `cv2.VideoWriter_fourcc(*'MJPG')`
  - 設定影片: `cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))` 
  
  ```python
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
  ```

## 畫圖
- line: `cv2.line(img, pt1, pt2, color, thickness)`
- rectangle: `cv.rectangle(	img, pt1, pt2, color, thickness)`
- circle: `cv2.circle(img, center, radius, color, thickness)`
- ellipse: `cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness)`
- polygon: `cv2.polylines(img, pts, isClosed, color, thickness) -> `
- text: `cv.putText(img, text, org, fontFace, fontScale, color, thickness`

```python
# line
cv2.line(img, (0,0), (512,512), (255,0,0), 2)

# rectangle
cv2.rectangle(img, (300,100), (400,200), (0,255,0), -1)

# circle
cv2.circle(img, (100,300), 75, (0,0,255), 4)

# ellipse
cv2.ellipse(img, (200,200), (100,50), 0, 0, 360, (255,255,0), -1)

# polygon
pts = np.array([[10,5],[20,30],[70,40],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255))

# text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OPENCV', (10,500),  font, 4, (255,255,255), 2, cv2.LINE_AA)
```

## 滑鼠偵測
- Callback: `cv2.setMouseCallback(winname,function)`
```python
def callback_function(event, x, y, flags, param):
  ...
```
- events: 
  - cv2.EVENT_FLAG_ALTKEY
  - cv2.EVENT_FLAG_CTRLKEY
  - cv2.EVENT_FLAG_LBUTTON
  - cv2.EVENT_FLAG_MBUTTON
  - cv2.EVENT_FLAG_RBUTTON
  - cv2.EVENT_FLAG_SHIFTKEY
  - cv2.EVENT_LBUTTONDBLCLK
  - cv2.EVENT_LBUTTONDOWN
  - cv2.EVENT_LBUTTONUP
  - cv2.EVENT_MBUTTONDBLCLK
  - cv2.EVENT_MBUTTONDOWN
  - cv2.EVENT_MBUTTONUP
  - cv2.EVENT_MOUSEHWHEEL
  - cv2.EVENT_MOUSEMOVE
  - cv2.EVENT_MOUSEWHEEL
  - cv2.EVENT_RBUTTONDBLCLK
  - cv2.EVENT_RBUTTONDOWN
  - cv2.EVENT_RBUTTONUP
  
## Trackbar
- create: `cv2.createTrackbar(name, winname, min, max, function)`
- get value: `cv2.getTrackbarPos(name, winname)`


