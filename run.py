import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2

# This line will download the model from the internet if it is not present on your computer
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

cap = cv2.VideoCapture(1)  # 0 for webcam, 1 and above for external cameras

while cap.isOpened():
    ret, frame = cap.read()

    # Make detections
    results = model(frame)

    cv2.imshow('YOLO', np.squeeze(results.render()))

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()
