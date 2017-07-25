import cv2
import numpy as np
import os
import subprocess
import pygame

cap = cv2.VideoCapture(1)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([100,130,130])
    upper_blue = np.array([130,255,255])
    

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    pygame.mixer.init()
    s = pygame.mixer.Sound("C:\cc\qwe.wav")

    
    x,y,w,h=cv2.boundingRect(mask)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    if x>30:
        s.play()
    else:
        pygame.mixer.music.pause()
    


    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
