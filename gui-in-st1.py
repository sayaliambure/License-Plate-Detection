import streamlit as st
import cv2
import numpy as np
import pandas as pd
from io import StringIO
from PIL import Image
import os
from streamlit.components.v1 import html
import subprocess

st.title("Number Plate Detection")
# st.write("Detection and Recognition of number plates using yolo algorithm")

def load_image(img):
    im = Image.open(img)
    image = np.array(im)
    return image


uploadFile = st.file_uploader(label="Choose a car image or video")

if uploadFile is not None:
    # Perform your Manupilations (In my Case applying Filters)
    img = load_image(uploadFile)
    st.image(img)
    st.write("Image Uploaded Successfully")
    file_details = {"FileName":uploadFile.name}
    # st.write(file_details)
else:
    st.write("Make sure you image is in JPG/PNG Format.")


# command = "python detect.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --images ./data/images/"+uploadFile.name+" --plate"

# if st.button(label="Output"):
    # st.write(file_details)
    # print(uploadFile.name)
    # print("python detect.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --images ./data/images/"+uploadFile.name+" --plate")

def open_terminal():
    if st.button('Open Terminal'):
        subprocess.Popen(['start', 'cmd'], shell=True)
        # subprocess.Popen(['start', 'cmd', '/k', 'echo', 'Command is {command}'], shell=True)
        # subprocess.Popen(['python', '-c', 'print("Hello World")'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        print("python detect.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --images ./data/images/"+uploadFile.name+" --plate")
open_terminal()