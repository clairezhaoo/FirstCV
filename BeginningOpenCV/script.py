from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2

def displayAndRemove(image, label, text):
    """Purpose is to show new image, close previous images, and write text on image, if any"""
    cv2.destroyAllWindows()
    # if text supplied, need to write it onto image
    if text != None:
        cv2.putText(image, text, (170, 180), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
    cv2.imshow(label, image)
    cv2.waitKey(0)


def overlay(background, foreground):
    """Purpose is to put one image on top of another by using masking, thresholding, and bitwise"""
    # keep copy of background
    backgroundCopy = background.copy()
    # ROI to add object
    rows, cols, channels = foreground.shape
    roi = background[0:rows, 0:cols]

    # make mask and inverse mask of object
    foregroundGray = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(foregroundGray, 253, 255, cv2.THRESH_BINARY_INV)
    mask_inv = cv2.bitwise_not(mask)

    # make black background ROI for object to be put in
    background_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

    # take object region from object image
    foreground_fg = cv2.bitwise_and(foreground, foreground, mask = mask)

    # put object in ROI and make modifications
    dst = cv2.add(background_bg, foreground_fg)
    background[0:rows, 0:cols] = dst

    return background, backgroundCopy


darkforestImage = cv2.imread("darkforest.png")
eggImage = cv2.imread("egg.png")
def onTrackbar(val):
    titleWindow = "Drag the flashlight bar to see in the dark forest."
    alpha_slider_max = 100

    alpha = val / alpha_slider_max
    beta = ( 1.0 - alpha )
    dst = cv2.addWeighted(eggImage, alpha, darkforestImage, beta, 0.0)
    cv2.imshow(titleWindow, dst)


def main():
    # path to all images
    bridgePath = "bridge.png"
    peppaPath = "peppa.png"
    welcomePath = "welcome.png"
    peppa1Path = "peppa1.png"
    peppa2Path = "peppa2.png"
    peppa3Path = "peppa3.png"
    peppa4Path = "peppa4.png"
    peppa5Path = "peppa5.png"
    darkforestPath = "darkforest.png"
    eggPath = "egg.png"

    # load all images
    bridgeImage = cv2.imread(bridgePath)
    peppaImage = cv2.imread(peppaPath)
    welcomeImage = cv2.imread(welcomePath)
    peppa1Image = cv2.imread(peppa1Path)
    peppa2Image = cv2.imread(peppa2Path)
    peppa3Image = cv2.imread(peppa3Path)
    peppa4Image = cv2.imread(peppa4Path)
    peppa5Image = cv2.imread(peppa5Path)
    darkforestImage = cv2.imread(darkforestPath)
    eggImage = cv2.imread(eggPath)

    # display welcome
    displayAndRemove(welcomeImage, "Welcome to Peppa's Lost Journey!", "Peppa is lost. Help her return home!")

    # list of peppas at different locations
    peppasMoves = [peppa1Image, peppa2Image, peppa3Image, peppa4Image, peppa5Image]
    # create peppa on bridge
    imagesCombined, bridgeCopy = overlay(bridgeImage, peppaImage)
    cv2.destroyAllWindows()
    cv2.imshow("Help Peppa cross this bridge with your keys (key D)!", imagesCombined)
    i = 0
    while(i <= 4):
        cv2.imshow("Help Peppa cross this bridge with your keys (key D)!", imagesCombined)
        k = cv2.waitKey(0)     # D key value is 100
        if k == 100:
            # move peppa over to the right
            currentPeppa = peppasMoves[i]
            imagesCombined, bridgeCopy = overlay(bridgeCopy, currentPeppa)
            i += 1   # increment peppas moves each time

    # next phase
    displayAndRemove(darkforestImage, "You made it across the bridge! Peppa is now in a dark forest (space bar)", None)
    titleWindow = "Drag the flashlight bar to see in the dark forest."
    alpha_slider_max = 100
    cv2.namedWindow(titleWindow)
    trackbarName = "Flashlight Slider"
    cv2.createTrackbar(trackbarName, titleWindow, 0, alpha_slider_max, onTrackbar)
    onTrackbar(0)
    cv2.waitKey(0)

    

main()
