# Clone YOLOv5 repository
!git clone https://github.com/ultralytics/yolov5  # clone repo
%cd yolov5
!git reset --hard 064365d8683fd002e9ad789c1e91fa3d021b44f0

# Install dependencies as necessary
!pip install -qr requirements.txt  # install dependencies (ignore errors)
import torch

from IPython.display import Image, clear_output  # to display images
from utils.downloads import attempt_download  # to download models/datasets

# clear_output()
print('Setup complete. Using torch %s %s' % (torch.__version__, torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU'))

import os
os.environ["DATASET_DIRECTORY"] = "/content/datasets"

# Install Roboflow
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key=<YOUR_API_KEY>)
project = rf.workspace("yolo-nznfs").project("yolo-dxgl2")
version = project.version(3)
dataset = version.download("yolov5")

# Training the model
!python train.py --img 416 --batch 16 --epochs 150 --data {dataset.location}/data.yaml --weights yolov5s.pt --name yolov5s_results --cache --device 0 --workers 8

# Inference
!python detect.py --weights runs/train/yolov5s_results/weights/best.pt --img 416 --conf 0.25 --source {dataset.location}/test/images/

# Display results
import glob
from IPython.display import Image, display

for imageName in glob.glob('/content/yolov5/runs/detect/exp/*.jpg'): # assuming JPG
    display(Image(filename=imageName))
    print("\n")
