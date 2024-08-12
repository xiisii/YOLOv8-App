import os
import cv2
import numpy as np
from tqdm import tqdm
import argparse
import fileinput

ROOT_DIR = os.getcwd()

# create dict to map class names to numbers for yolo
classes = {}
with open("classes.txt", "r") as myFile:
    for num, line in enumerate(myFile, 0):
        line = line.rstrip("\n")
        classes[line] = num
    myFile.close()

# step into dataset directory
os.chdir('C:/Users/hvthy/Desktop/DoAn2/SEGMENTATION/Data/Data_v7/Dataset/labels')
DIRS = os.getcwd()
DIRS1 = os.listdir(os.getcwd())

for DIR in DIRS1:
    if os.path.isdir(DIR):
        os.chdir(DIR)
        DIRS2 = os.getcwd()
        print("Currently in subdirectory:", DIR)
        for filename in tqdm(os.listdir(os.getcwd())):
            filename_path=os.path.join(DIRS2, filename)
            annotations = []
            with open(filename_path,'r') as f:
                for line in f:
                    for class_type in classes:
                        line = line.replace(class_type, str(classes.get(class_type)))
                    labels = line.split()
                    coords = np.asarray([float(labels[1]), float(labels[2]), float(labels[3]), float(labels[4])])
                    labels[1], labels[2], labels[3], labels[4] = coords[0], coords[1], coords[2], coords[3]
                    newline = str(labels[0]) + " " + str(labels[1]) + " " + str(labels[2]) + " " + str(labels[3]) + " " + str(labels[4])
                    line = line.replace(line, newline)
                    annotations.append(line)
                f.close()
            with open(filename_path, "w",encoding='utf-8') as outfile:
                for line in annotations:
                    outfile.write(line)
                outfile.close()
    os.chdir(DIRS)

