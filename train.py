from ultralytics import YOLO

YOLO("yolov8n.yaml").train(data="coco128.yaml", epochs=3)
