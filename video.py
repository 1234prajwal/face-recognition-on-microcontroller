import numpy as np
import cv2
from createpnet import *

cap = cv2.VideoCapture(0)
 
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,1)
    output = detectFace(gray, 0.7)
    if output == []:
        print("No face found")
    elif isinstance(output[0], list) :
        x,y,x1,y1=int(output[0][0]),int(output[0][1]),int(output[0][2]),int(output[0][3])
        gray = cv2.rectangle(gray, (x,y), (x1,y1), (255, 255, 0), 3)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
