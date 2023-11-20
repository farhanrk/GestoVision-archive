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
import cv2 as cv
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
    #Using tkinter object to open a file dialogue to browse for the photo 
    #We'll use openCV ui primarily to display the picture
    #Creating and hiding a tk object because otherwise the picture window disappears for some reason
    window = tk.Tk()
    window.withdraw()
    img_path = filedialog.askopenfilename(title="Select an Image!") # Opening a dialogue box to browse and open the image we want to work with.

    #Running the program if the selected path to the image is valid
    if img_path:
        # Reading and showing the image
        img = cv.imread(img_path)
        cv.imshow("The image (press any button to continue)", img)
        print("Image loaded and shown.")
        cv.waitKey(0) #waiting for a keey press 
        cv.destroyAllWindows()


    else:
        print("No image selected.")
        

#For running the program from terminal
if __name__ == "__main__":
    main()
