import cv2
import numpy as np
from PIL import ImageGrab
from mss import mss
import SendKeys
import time
from datetime import datetime

cod = []
accel = 170
counta = 0

def findDino():
    time.sleep(3)
    dinoimg = cv2.imread('dino.png', 0)
    w, h = dinoimg.shape[::-1]

    img = ImageGrab.grab()
    imgcv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    imgcv  = cv2.cvtColor(imgcv, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(imgcv, dinoimg, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    global cod
    cod = [top_left[1] + 86, bottom_right[1] - 40, top_left[0] + 450, bottom_right[0] + 350]


def pular():
    send = "{SPACE}"
    SendKeys.SendKeys(send)

def ajustaImg():
    monitor = {'top': cod[1] - 100, 'left': cod[2] - int(accel), 'width': 10, 'height': 100}
    with mss() as sct:
        imgcv = np.array(sct.grab(monitor))

    imgcv = cv2.cvtColor(imgcv, cv2.COLOR_BGR2GRAY)
    _, imgcv = cv2.threshold(imgcv, 128, 255, cv2.THRESH_BINARY)

    #cv2.imwrite("kappa"+str(counta)+".png", imgcv)
    #global counta
    #counta += 1

    tempoflag = {'top': cod[1] + 100, 'left': cod[2] - int(accel), 'width': 10, 'height': 10}
    with mss() as sct:
        imgflag = np.array(sct.grab(tempoflag))

    imgflag = cv2.cvtColor(imgflag, cv2.COLOR_BGR2GRAY)
    _, imgflag = cv2.threshold(imgflag, 128, 255, cv2.THRESH_BINARY)

    if cv2.countNonZero(imgflag) > 80:
        if cv2.countNonZero(imgcv) < 900:
            # print("Jump")
            pular()
    else:
        if cv2.countNonZero(imgcv) > 20:
            # print("Jump")
            pular()

def tirarPrint():
    findDino()
    dt = datetime.now().second
    count = 0
    global accel
    accel += 0.05
    while (1):
        if dt != datetime.now().second:
            print(count)
            count = 0
            dt = datetime.now().second
        ajustaImg()
        count += 1


tirarPrint()

""" 
  DEBUG DE FPSTRABSON  

def tirarPri nt():
  cod = findDino()
  dt = datetime.now().second
  count = 0 
  while(1):
    if dt != datetime.now().second:
      print (count)
      count = 0
      dt = datetime.now().second
    ajustaImg(cod)
    count += 1
"""
