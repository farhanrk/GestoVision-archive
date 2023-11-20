###################################________GestoVision________###################################
##
##  Project || CS 3301 - Visual Computing
##  Group Name          : The Trainers
##  Group Members(s)    : [Trishir Kumar Singh, Farhan Rahman Khan] 
##  Name                : Trishir Kumar Singh
##  Student ID          : 202023149
##  Name                : Farhan Rahman Khan
##  Student ID          : 202124798
#####################################||IMPORTING LIBRARIES||#####################################
import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
import numpy as np
import math
from matplotlib import pyplot as plt
import mediapipe as mp


#################################################################################################

def main():
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    # Initialize MediaPipe Hands
    hands = mp_hands.Hands()
    # Initialize media capture
    cap = cv2.VideoCapture(1)
    while True:
        # Get frame
        success, frame = cap.read()
        if not success:
            break

        # Process the image and get hand landmarks
        results = hands.process(frame)

        # Draw landmarks on the image
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
        cv2.imshow("Image", frame)
        key_press = cv2.waitKey(1)
        if not key_press == -1:
            break
    cap.release()
    cv2.destroyAllWindows()


# For running the program from terminal
if __name__ == "__main__":
    main()
