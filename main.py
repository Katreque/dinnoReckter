import cv2
from PIL import ImageGrab


def tirarPrint():
  img = ImageGrab.grab()
  return img.save('screenshot.png')


tirarPrint()