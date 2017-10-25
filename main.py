import cv2
import numpy as np
from PIL import ImageGrab
from time import sleep

def ajustaImg():
  img = cv2.imread('screenshot.png')
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  kernel = np.ones((1, 1), np.uint8)
  img = cv2.dilate(img, kernel, iterations=1)
  img = cv2.erode(img, kernel, iterations=1)
  img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

  cv2.imwrite("screenshot.png", img)

def tirarPrint():
  while(1):
    img = ImageGrab.grab()
    img.save('screenshot.png')
    ajustaImg()
    sleep(0.03)



tirarPrint()