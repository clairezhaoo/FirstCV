import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# define a matrix M. tells how many pixels left right, up down, to be shifted
M = np.float32([[1, 0, 25], [0, 1, 50]])   # floating point array  [1,0,tx][0,1,ty]
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0])) # manually supply dimensions of image
cv2.imshow("Shifted Right and Down", shifted)   # show results of translation

M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Left and Up", shifted)
shifted = imutils.translate(image, 0, 100)   # using convenience method from imutils.py
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)
