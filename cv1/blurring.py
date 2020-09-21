import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# a sliding window, or kernel
blurred = np.hstack([
    cv2.blur(image, (3, 3)),   # average blurring
    cv2.blur(image, (5, 5)),   # increase in size of kernel leads to more blurring
    cv2.blur(image, (7, 7))])
cv2.imshow("Average", blurred)
cv2.waitKey(0)

blurred = np.hstack([
    cv2.GaussianBlur(image, (3, 3), 0),   # gaussian blurring
    cv2.GaussianBlur(image, (5, 5), 0),   # tuple represents kernel size, increasing
    cv2.GaussianBlur(image, (7, 7), 0)])  # last parameter is standard deviation in the x-axis direction
cv2.imshow("Gaussian", blurred)           # 0 means auto compute based on kernel size
cv2.waitKey(0)                            # gaussian has less blur, and more natural b/c weighted average

blurred = np.hstack([
    cv2.medianBlur(image, 3),   # median blurring
    cv2.medianBlur(image, 5),   # takes size of kernel (k, k x k)
    cv2.medianBlur(image, 7)])  # replace central pixel with median of neighborhood
cv2.imshow("Median", blurred)   # removes salt and pepper noise
cv2.waitKey(0)

blurred = np.hstack([
    cv2.bilateralFilter(image, 5, 21, 21),   # bilateral blurring
    cv2.bilateralFilter(image, 7, 31, 31),   # takes diameter of nbh and color and space deviation
    cv2.bilateralFilter(image, 9, 41, 41)])  # preserve edges whil reducing noise
cv2.imshow("Bilateral", blurred)   # removes salt and pepper noise
cv2.waitKey(0)
