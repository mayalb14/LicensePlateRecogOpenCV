# he poppin pillis makin millis droppin fillies, hi and welcome to chillis

# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument(
    "-i", "--image", required=True, help="path to input image to be OCR'd")
ap.add_argument(
    "-p", "--preprocess", type=str, default="thresh",
    help="type of preprocessing to be done")
args = vars(ap.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread("")  # path to image here
processedPicture = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if args["preprocess"] == "thresh":
    processedPicture = cv2.threshold(
        processedPicture, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

elif args["preprocess"] == "blur":
    processedPicture = cv2.medianBlur(processedPicture, 3)

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, processedPicture)
cv2.imshow("Image", image)
cv2.imshow("Output", processedPicture)
cv2.waitKey(0)

text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

cv2.imshow("Image", image)
cv2.imshow("Output", processedPicture)
cv2.waitKey(0)
