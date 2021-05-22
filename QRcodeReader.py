import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread('qrcode.jpg')
cap = cv2.VideoCapture(0)
# cap.open('http://192.168.1.203:8080/video')

while cap.isOpened():
    success, img = cap.read()

    for barcode in decode(img):
        print(barcode.data)
        myData = barcode.data.decode('utf')
        print(myData)
        points = np.array([barcode.polygon], np.int32)
        points = points.reshape((-1, 1, 2))
        cv2.polylines(img, [points], True, (255, 0, 255), 3)
        points2 = barcode.rect
        cv2.putText(img, myData, (points2[0], points2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255),2)

    cv2.imshow('scanner',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()