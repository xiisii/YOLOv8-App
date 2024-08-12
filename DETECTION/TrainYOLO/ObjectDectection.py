#Object Dectection

from ultralytics import YOLO

if __name__ == '__main__':
    # build a new model from scratch
    model = YOLO("yolov8n.yaml") 
    results= model.train(data="config.yaml", epochs=100, device='0')   # train the model
    


