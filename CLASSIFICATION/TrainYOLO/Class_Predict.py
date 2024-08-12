from ultralytics import YOLO

import numpy as np


model = YOLO('./runs/classify/train/weights/last.pt')  # load a custom model

results = model('C:/Users/hvthy/Downloads/Banana.jpg')  # predict on an image

names_dict = results[0].names

probs = results[0].probs.data.tolist()

print(names_dict)
print(probs)

print(names_dict[np.argmax(probs)])
