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
  img = img.crop((460, 537, 470,  547))
  img.save('./S.png')

  img = cv2.imread('./S.png')
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  cv2.imwrite("./S.png", img)

  img = Image.open('./S.png').convert('L')
  if not img.getbbox():
    print('Yep!')
    pular()
  else:
    print('Noup!')

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

