from __future__ import print_function
import argparse
import cv2
# path = ./trex.png
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image") # argument is path to image on disk
args = vars(ap.parse_args())    # parse arguments and store in dictionary

image = cv2.imread(args["image"])    # load image off disk with path to image and imread
print("width: {} pixels".format(image.shape[1])) # examine dimensions of the image. use NumPy array format and shape attribute
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

cv2.imshow("Image", image)  # name of window, reference to image
cv2.waitKey(0) # execution after key is pressed, 0 means any key
cv2.imwrite("newimage.jpg", image)  # write and ssave image in JPG format
