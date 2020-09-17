import mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
ap.add_argument("-s", "--size", required = False, help = "Size of largest color bin", default  = 5000)
ap.add_argument("-b", "--bins", required = False, help = "Num bins per color channel", default  = 8)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
size = float(args["size"])
bins = int(args["bins"])

hist = cv2.calcHist([image], [0, 1, 2], None, [bins, bins, bins], [0, 256, 0, 256, 0, 256])

print("3D histogram shape: %s, with %d values" % (hist.shape, hist.flatten().shape[0]))
