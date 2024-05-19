import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
import pytesseract
from datetime import datetime
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


model = YOLO('yolov8/best.pt')

# Defines a callback function to print the mouse coordinates 
# when the mouse moves over the window named 'RGB'
def RGB(event, x, y, flags, param):
  if event == cv2.EVENT_MOUSEMOVE:
    point = [x, y]
#     print(point)

# cv2.namedWindow('RGB')
# cv2.setMouseCallback('RGB', RGB)


cap = cv2.VideoCapture('yolov8/videos/mycarplate.mp4')

my_file = open('yolov8/coco.txt', 'r')
# Reads class names from a file and splits them into a list
data = my_file.read()
class_list = data.split('\n')

# Defines a polygonal region of interest for detection.
area = [(27, 417), (16, 456), (1015, 451), (992, 417)]

# Initializes counters and list & set to keep track of detected plates and ensure they are logged only once
count = 0
list1 = []
processed_numbers = set()

# Open file for writing car plate data
with open("yolov8/car_plate_data.txt", "a") as file:
  file.write("NumberPlate\tDate\tTime\n")  # Writing column headers



while True:    
  # Reads frames from the video.
  ret, frame = cap.read()
  count += 1
  # Processes every third frame to reduce processing load.
  if count % 6 != 0:
    continue
  if not ret:
    break
  
  # Resizes the frame.
  frame = cv2.resize(frame, (1020, 500))
  # Runs the YOLO model on the frame to detect objects.
  results = model.predict(frame)
  # boxes refers to the detected bounding boxes, and data holds the actual numerical data for these boxes.
  a = results[0].boxes.data
  # converts the bounding box data (a) into a Pandas DataFrame
  px = pd.DataFrame(a).astype("float")
  
  # Iterates over detected bounding boxes.
  for index, row in px.iterrows():
    # x1,y1 - Coordinates of the top-left corner of the bounding box.
    x1 = int(row[0])
    y1 = int(row[1])
    #  Coordinates of the bottom-right corner of the bounding box
    x2 = int(row[2])
    y2 = int(row[3])
    
    # This is the class index of the detected object, extracted from the row of the DataFrame (px)
    d = int(row[5])
    # Retrieves the class label from the class_list
    c = class_list[d]
    # Calculating the Center of the Bounding Box
    cx = int(x1 + x2) // 2
    cy = int(y1 + y2) // 2
    # Checking if the Center is Within the Defined Area
    result = cv2.pointPolygonTest(np.array(area, np.int32), ((cx, cy)), False)
    if result >= 0:
    #   Crops the detected license plate region.
      crop = frame[y1:y2, x1:x2]
      # Converts it to grayscale and applies a bilateral filter.
      gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
      gray = cv2.bilateralFilter(gray, 10, 20, 20)

      # Extracts text using Tesseract OCR.
      text = pytesseract.image_to_string(gray).strip()
      # Define a translation table to remove specific characters
      remove_chars = "()[],|/_\'\"“‘"
      translation_table = str.maketrans('', '', remove_chars)

      # Use the translation table to remove the characters
      text = text.translate(translation_table)
      text = text.replace(' ', '')
      # Cleans and logs the detected text if it hasn't been processed before
      if text and text not in processed_numbers:
        processed_numbers.add(text) 
        list1.append(text)
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("yolov8/car_plate_data.txt", "a") as file:
          file.write(f"{text}\t{current_datetime}\n")
          cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
          cv2.imshow('crop', crop)

  # Draws the detection area polygon on the frame
  cv2.polylines(frame, [np.array(area, np.int32)], True, (255, 0, 0), 2)
  # Displays the frame and cropped plate images
  cv2.imshow("RGB", frame)
  # Exits the loop if the 'Esc' key is pressed
  if cv2.waitKey(1) & 0xFF == 27:
    break

cap.release()    
cv2.destroyAllWindows()
