import cv2
import numpy as np
from PIL import ImageGrab
import SendKeys
import time
from datetime import datetime


def findDino():
  time.sleep(3)
  dinoimg = cv2.imread('dino.png', 0)
  w, h = dinoimg.shape[::-1]

  img = ImageGrab.grab()
  imgcv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
  imgcv = cv2.cvtColor(imgcv, cv2.COLOR_BGR2GRAY)

  res = cv2.matchTemplate(imgcv, dinoimg, cv2.TM_CCOEFF)
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
  top_left = max_loc
  bottom_right = (top_left[0] + w, top_left[1] + h)

  cv2.rectangle(imgcv, top_left, bottom_right, 0, 2)
  cv2.rectangle(imgcv, (top_left[0] + 450, top_left[1] + 53), (bottom_right[0] + 350, bottom_right[1] - 53), 0, 2)
  cv2.imwrite("match.png", imgcv)

  return [top_left[1] + 53, bottom_right[1] - 53, top_left[0] + 450, bottom_right[0] + 350]

def pular():
  send = "{SPACE}"
  SendKeys.SendKeys(send)

def ajustaImg(cod):
  img = ImageGrab.grab()

  imgcv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
  imgcv = cv2.cvtColor(imgcv, cv2.COLOR_BGR2GRAY)
  _,imgcv = cv2.threshold(imgcv, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

  imgcort = imgcv[cod[0]:cod[1], cod[2]:cod[3]]
  cv2.imwrite("s.png", imgcort)

  if cv2.countNonZero(imgcort) < 10:
    print("Jump")
    pular()

def tirarPrint():
  cod = findDino()
  print cod
  while(1):
    ajustaImg(cod)


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
