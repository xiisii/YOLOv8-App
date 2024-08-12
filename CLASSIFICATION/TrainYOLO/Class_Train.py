from ultralytics import YOLO
if __name__ == "__main__":
    model = YOLO('yolov8n-cls.pt')  # load a pretrained model (recommended for training)
    model.train(data='C:/Users/hvthy/Desktop/DoAn2/CLASSIFICATION/Data/Dataset',epochs=100, imgsz=64)
