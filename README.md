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

> It is suggested that you should create a virtual environment for this reporsitory. You can use `Anaconda` to create it.

#### Create a virtual environment

```bash
conda create -n <env_name> python=3.9 # Note: <env_name> is the name of your virtual environment
# For example: conda create -n myyolo python=3.9
```

#### Activate your virtual environment and install the requirements

```bash
cd yolov5 # change directory to yolov5
conda activate <env_name> # activate your virtual environment
pip install -r requirements.txt
```

## How to use

Just run the `run.py`. (Make sure your camera is available)

Click `Q` to quit the program.