import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Originial", image)
# aspect ratio computation
r = 150.0 / image.shape[1]    # pick new image to be 150 px wide and divide by width for ratio
dim = 150, int(image.shape[0] * r)  # new dimensions. height found with ratio
# resizing image. interpolation method handles resizing
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)
r = 50.0 / image.shape[0]   # another ratio r using height. this time use to find width
dim = (int(image.shape[1] * r), 50)

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)
resized = imutils.resize(image, width = 100)
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)
