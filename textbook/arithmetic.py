import numpy as np
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# opencv uses clipping to preserve range 0-255
print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))
print("wrap around: {}".format(np.uint8([200]) + np.uint8([100]))) # numpy uses modulo arithemtic and wraps around
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

M = np.ones(image.shape, dtype = "uint8") * 100  # NP array of ones, fill with values of 100
added = cv2.add(image, M)    # add matrix of 100s to original image, increase px intensity
cv2.imshow("Added", added)   # "washed out" image
cv2.waitKey(0)
M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted) # darker image
cv2.waitKey(0)
