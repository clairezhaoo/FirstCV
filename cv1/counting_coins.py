import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)  # blurring removes "noisy" edges, only need to find outlines
cv2.imshow("Image", image)
# parameters: blurred and grayscale image, threshold 1, threshold 2
edged = cv2.Canny(image, 30, 150)    # below 30 not edge, greater than 150 and in between is edge
cv2.imshow("Edges", edged)
cv2.waitKey(0)
# returns 3-tuple of destructed image after contour, contours (cnts), hierarchy of contours
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("I count {} coins in this image".format(len(cnts)))

coins = image.copy()
cv2.drawCountours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)
