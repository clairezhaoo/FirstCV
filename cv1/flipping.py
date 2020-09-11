import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# flip function requires image to flip and flip code
flipped = cv2.flip(image, 1)    # flip code = 1, horizontal
cv2.imshow("Flipped Horizontally", flipped)

flipped = cv2.flip(image, 0)    # flip code = 0, vertical
cv2.imshow("Flipped Vertically", flipped)

flipped = cv2.flip(image, -1)   # flip code = -1, both axes
cv2.imshow("Flipped Horizontally and Vertically", flipped)
cv2.waitKey(0)
