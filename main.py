# he poppin pillis makin millis droppin fillies, hi and welcome to chillis

# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os

# load the example image and convert it to grayscale
image = cv2.imread("")  # path to image here
processedPicture = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, processedPicture)

text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)
