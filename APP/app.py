#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   @File Name:     app.py
   @Author:        Luyao.zhang
   @Date:          2023/5/15
   @Description:
-------------------------------------------------
"""
from pathlib import Path
from PIL import Image
import streamlit as st

import config
from utils import load_model, infer_uploaded_image, infer_uploaded_video, infer_uploaded_webcam

# setting page layout
st.set_page_config(
    page_title="Interactive Interface for YOLOv8",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
    )

# main page heading
st.title("Interactive Interface for YOLOv8")

# sidebar
st.sidebar.header("DL Model Config")

# model options
task_type = st.sidebar.selectbox(
    "Select Task",
    ["Detection",
     "Classification",
     "Segmentation",
     "Tracking",
     "Pose Estimation"]
)

model_type = None
if task_type == "Detection":
    model_type = st.sidebar.selectbox(
        "Select Model",
        config.DETECTION_MODEL_LIST
    )
elif task_type == "Classification":
    model_type = st.sidebar.selectbox(
        "Select Model",
        config.CLASS_MODEL_LIST
    )
elif task_type == "Segmentation":
    model_type = st.sidebar.selectbox(
        "Select Model",
        config.SEG_MODEL_LIST
    )
elif task_type == "Tracking":
    model_type = st.sidebar.selectbox(
        "Select Model",
        config.DETECTION_MODEL_LIST
    )
elif task_type == "Pose Estimation":
    model_type = st.sidebar.selectbox(
        "Select Model",
        config.POSE_MODEL_LIST
    )
else:
    st.error("Currently only 'Detection' function is implemented")

confidence = float(st.sidebar.slider(
    "Select Model Confidence", 30, 100, 50)) / 100

model_path = ""
if model_type == 'best.pt':
    model_path = 'C:/Users/hvthy/Desktop/DoAn2/DETECTION/TrainYOLO/runs/detect/train/weights/best.pt'
else:
    model_path = Path(config.MODEL_DIR, str(model_type))


# load pretrained DL model
model = load_model(model_path)


# image/video options
st.sidebar.header("Image/Video Config")
source_selectbox = st.sidebar.selectbox(
    "Select Source",
    config.SOURCES_LIST
)

source_img = None
if source_selectbox == config.SOURCES_LIST[0]: # Image
    infer_uploaded_image(confidence, model, task_type)
elif source_selectbox == config.SOURCES_LIST[1]: # Video
    infer_uploaded_video(confidence, model)
elif source_selectbox == config.SOURCES_LIST[2]: # Webcam
    infer_uploaded_webcam(confidence, model, task_type)
else:
    st.error("Currently only 'Image' and 'Video' source are implemented")