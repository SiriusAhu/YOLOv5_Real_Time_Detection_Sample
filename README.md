## Introduction
This reporsitory is a sample of yolo real-time object detection.

It only provides basic functions of yolo and camera capture.

## Requirements

To run this reporsitory, you need to follow the steps one by one.

As for the environment, I suggest using `python>=3.8`.

### Step 1: Clone yolov5 reporsitory

Since this model require `pytorch`, please make sure you have GPU support.(`pytorch CPU` version is also OK, but with lower efficiency)

```bash
git clone https://github.com/ultralytics/yolov5
```

### Step 2: Install the requirements of yolov5

```bash
cd yolov5 # change directory to yolov5
pip install -r requirements.txt
```

## How to use

Just run the `run.py`. (Make sure your camera is available)



Click `Q` to quit the program.