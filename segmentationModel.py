#Will run the segmentation model yolov8n-seg
from ultralytics import YOLO
model = YOLO("yolov8n-seg.pt")
model.info()
results = model.predict(0, save=False, show=True)