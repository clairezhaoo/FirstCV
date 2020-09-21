from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2
# load all images
entrancePath = "entrance.png"
peppaPath = "peppa.png"
entranceImage = cv2.imread(entrancePath, -1)  # -1 for IMAGE_UNCHANGED
peppaImage = cv2.imread(peppaPath, -1)
# display background
cv2.imshow("Image", entranceImage)
cv2.waitKey(0)

# ROI to add peppa
rows, cols, channels = peppaImage.shape
roi = entranceImage[0:rows, 0:cols]

# make mask and inverse mask of peppa
peppaImageGray = cv2.cvtColor(peppaImage, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(peppaImageGray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# make black background for peppa to be in
entranceImage_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

# take peppa region from peppa image
peppaImage_fg = cv2.bitwise_and(peppaImage, peppaImage, mask = mask)

# put peppa in ROI and make modifications
dst = cv2.add(entranceImage_bg, peppaImage,_fg)
entranceImage[0:rows, 0:cols] = dst

cv2.imshow("res", entranceImage)
cv2.waitKey(0)
