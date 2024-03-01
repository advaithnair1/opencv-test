import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Filter colors using Numpy arrays
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
   
    filter_mask = cv2.inRange(hsv, lower_red, upper_red)

    # Filter colors using Numpy arrays (hue)
    lower_red = np.array([170, 100, 100])
    upper_red = np.array([180, 255, 255])
    color_mask = cv2.inRange(hsv, lower_red, upper_red)

    mask = filter_mask + color_mask

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Original', frame)
    cv2.imshow('Red Mask', result)

    if cv2.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv2.destroyAllWindows()
