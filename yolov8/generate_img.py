import cv2
import time
cpt = 0     # A counter for the number of frames saved.
maxFrames = 120   

count = 0   # counter to keep track of the frames processed.
cap = cv2.VideoCapture(r'D:/VS Code/Data science/Projects/License plate recognition/yolov8/mycarplate.mp4')

while cpt < maxFrames:
  ret, frame = cap.read()    # Captures a frame from the video.
  if not ret:
    break
  count += 1
  if count % 3 != 0:   # Only process every third frame. This skips two out of every three frames.
    continue
  frame = cv2.resize(frame, (1080, 500))
  cv2.imshow('test window', frame)    
  cv2.imwrite(r'D:/VS Code/Data science/Projects/License plate recognition/yolov8/images/img%d.jpg'%cpt, frame)   # Save the frame as an image file. The filename includes the frame count (cpt)
  time.sleep(0.01)
  cpt += 1
  if cv2.waitKey(5)&0xFF==27:   #Exit the loop if the 'Esc' key (ASCII 27) is pressed.
    break
cap.release()
cv2.destroyAllWindows()