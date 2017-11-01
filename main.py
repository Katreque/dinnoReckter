import cv2
import numpy as np
from PIL import ImageGrab, Image
import SendKeys

def pular():
  send = "{SPACE}"
  SendKeys.SendKeys(send)

def ajustaImg():
  img = Image.open('S.png').convert('L')
  img = img.crop((265, 345, 285, 365))
  img.save('S.png')

  img = cv2.imread('S.png')
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  cv2.imwrite("S.png", img)

  img = Image.open('S.png').convert('L')
  if not img.getbbox():
    print('Yep!')
    pular()
  else:
    print('Noup!')


def tirarPrint():
  while(1):
    img = ImageGrab.grab()
    img.save('S.png')
    ajustaImg()

tirarPrint()