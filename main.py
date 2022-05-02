import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0) # OpenCV Video capture object using webcam 0

while True:
    success, img = cap.read() # Grabs, decodes and returns a success (Bool) flag, and the next video frame

    cv2.imshow("Image", img) # Display the read image
    cv2.waitKey(1) # Wait until key one is pressed