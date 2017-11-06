import cv2
import numpy as np
from PIL import ImageGrab, Image
import SendKeys
from datetime import datetime


def pular():
  send = "{SPACE}"
  SendKeys.SendKeys(send)


def ajustaImg():
  img = ImageGrab.grab()

  imgcv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
  imgcv = cv2.cvtColor(imgcv, cv2.COLOR_BGR2GRAY)
  _,imgcv = cv2.threshold(imgcv, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

  crop_img = imgcv[485:495, 575:585]
  cv2.imwrite("s.png", crop_img)

  if cv2.countNonZero(crop_img) < -1:
    print("Jump")
    pular()


def tirarPrint():
  while (1):
    ajustaImg()


tirarPrint()

"""
  DEBUG DE FPSTRABSON

def tirarPrint():
  dt = datetime.now().second
  count = 0
  while(1):
    if dt != datetime.now().second:
      print(count)
      count = 0
      dt = datetime.now().second
    ajustaImg()
    count += 1
"""
