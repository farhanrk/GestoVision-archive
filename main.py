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
    cap = cv2.VideoCapture(1)
    while True:
        success, img = cap.read()
        if not success:
            break
        cv2.imshow("Image", img)
        cv2.waitKey(30)
    cap.release()
    cv2.destroyAllWindows()


# For running the program from terminal
if __name__ == "__main__":
    main()
