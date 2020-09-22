import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # usually compute gradients on single channel, grayscale
cv2.imshow("Image", image)

lap = cv2.Laplacian(image, cv2.CV_64F) # 64-bit float for (neg values) transition of black-to-white and white-to-black
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)
# compute gradient magnitude representations along both axes
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0) # horizontal edge-like regions
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1) # vertical edge-like regions
# find all edges, absolute value of all edges, convert to 8-bit
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)   # pixel will be true when either edge is present

cv2.imshow("SobelX", sobelX)
cv2.imshow("SobelY", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)
