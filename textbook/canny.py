import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)  # blurring removes "noisy" edges, only need to find outlines
cv2.imshow("Blurred", image)
# parameters: blurred and grayscale image, threshold 1, threshold 2
canny = cv2.Canny(image, 30, 150)    # below 30 not edge, greater than 150 and in between is edge
cv2.imshow("Canny", canny)
cv2.waitKey(0)
