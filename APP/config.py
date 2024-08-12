#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   @File Name:     config.py
   @Author:        Luyao.zhang
   @Date:          2023/5/16
   @Description: configuration file
-------------------------------------------------
"""
from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())


# Source
SOURCES_LIST = ["Image", "Video", "Webcam"]


# DL model config
MODEL_DIR = ROOT
YOLOv8n = MODEL_DIR / "weights/detection/yolov8n.pt"
YOLOv8s = MODEL_DIR / "weights/detection/yolov8s.pt"
YOLOv8m = MODEL_DIR / "weights/detection/yolov8m.pt"
YOLOv8l = MODEL_DIR / "weights/detection/yolov8l.pt"
YOLOv8x = MODEL_DIR / "weights/detection/yolov8x.pt"
CustomData = "C:/Users/hvthy/Desktop/DoAn2/DETECTION/TrainYOLO/runs/detect/train/weights/best.pt"

DETECTION_MODEL_LIST = [
    "yolov8n.pt",
    "yolov8s.pt",
    "yolov8m.pt",
    "yolov8l.pt",
    "yolov8x.pt",
    "best.pt"]

YOLOv8ncls = MODEL_DIR / "weights/detection/yolov8n-cls.pt"
YOLOv8scls = MODEL_DIR / "weights/detection/yolov8s-cls.pt"
YOLOv8mcls = MODEL_DIR / "weights/detection/yolov8m-cls.pt"
YOLOv8lcls = MODEL_DIR / "weights/detection/yolov8l-cls.pt"
YOLOv8xcls = MODEL_DIR / "weights/detection/yolov8x-cls.pt"
CustomDatacls = "C:/Users/hvthy/Desktop/DoAn2/DETECTION/TrainYOLO/runs/detect/train/weights/best.pt"

CLASS_MODEL_LIST = [
    "yolov8n-cls.pt",
    "yolov8s-cls.pt",
    "yolov8m-cls.pt",
    "yolov8l-cls.pt",
    "yolov8x-cls.pt",
    "best-cls.pt"]

YOLOv8nseg = MODEL_DIR / "weights/detection/yolov8n-seg.pt"
YOLOv8sseg = MODEL_DIR / "weights/detection/yolov8s-seg.pt"
YOLOv8mseg = MODEL_DIR / "weights/detection/yolov8m-seg.pt"
YOLOv8lseg = MODEL_DIR / "weights/detection/yolov8l-seg.pt"
YOLOv8xseg = MODEL_DIR / "weights/detection/yolov8x-seg.pt"
CustomDataseg = "C:/Users/hvthy/Desktop/DoAn2/DETECTION/TrainYOLO/runs/detect/train/weights/best.pt"

SEG_MODEL_LIST = [
    "yolov8n-seg.pt",
    "yolov8s-seg.pt",
    "yolov8m-seg.pt",
    "yolov8l-seg.pt",
    "yolov8x-seg.pt",
    "best-seg.pt"]

YOLOv8npose = MODEL_DIR / "weights/detection/yolov8n-pose.pt"
YOLOv8spose = MODEL_DIR / "weights/detection/yolov8s-pose.pt"
YOLOv8mpose = MODEL_DIR / "weights/detection/yolov8m-pose.pt"
YOLOv8lpose = MODEL_DIR / "weights/detection/yolov8l-pose.pt"
YOLOv8xpose = MODEL_DIR / "weights/detection/yolov8x-pose.pt"
CustomDatapose = "C:/Users/hvthy/Desktop/DoAn2/DETECTION/TrainYOLO/runs/detect/train/weights/best.pt"

POSE_MODEL_LIST = [
    "yolov8n-pose.pt",
    "yolov8s-pose.pt",
    "yolov8m-pose.pt",
    "yolov8l-pose.pt",
    "yolov8x-pose.pt",
    "best-pose.pt"]