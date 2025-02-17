# REAL TIME ROAD LANE DETECTION

import cv2
import os
import numpy as np

# Load the video
src = cv2.VideoCapture('/Users/jane/Desktop/dev/OpenCV/data/drive_cam.mp4')

while True:
    ret, frame = src.read()
    
    if not ret:
        break
    
    # Get the frame dimensions (height, width)
    height, width, _ = frame.shape
    # bottom half of the frame + Canny Edge
    roi = frame[height//2:height, 0:width]
    gray_frame = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    edges = cv2.Canny(gray_frame, 50, 150)  # Apply Canny Edge Detection


    cv2.imshow('Canny Edge Video', edges)
    cv2.imshow('Original Video', frame)


    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

src.release()
cv2.destroyAllWindows()


# Region of Angle
