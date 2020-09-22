from __future__ import print_function
import argparse
import cv2
# setting up argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
# loading image off disk and displaying
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# accessing pixels
(b, g, r) = image[0, 0]  # grab pixel at point. represented as tuple
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
# manipulating pixels
image[0,0] = (0, 0, 225)  # set point to a new bgr value, red
(b, g, r) = image[0,0]  # grab pixel value
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))  # print changed pixel values
corner = image[0:100, 0:100]  # grabbing a 100x100 pixel region (top left corner)
cv2.imshow("Corner", corner)  # image that is result of cropping
# 4 indexes, start and stop for x and y
image[0:100, 0:100] = (0, 255, 0)    # change color of a region of pixels

cv2.imshow("Updated", image)
cv2.waitKey(0)
