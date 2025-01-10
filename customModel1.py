import cv2
from ultralytics import YOLO
model = YOLO("path to your model")
model.info()
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()  
    results = model.predict(source=frame, save=False, verbose=False)
    annotated_frame = results[0].plot() 
    cv2.imshow("Object Detection Model", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break
cap.release()
cv2.destroyAllWindows()
