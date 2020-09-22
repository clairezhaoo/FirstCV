import numpy as np
import cv2
# manually initialize image, with zeros method 0 every element starts at 0
canvas = np.zeros((300, 300, 3), dtype = "uint8") # 300 rows and columns, 3 channels for rgb, 8 bit int
green = (0, 255, 0)  # make tupe for "green"
cv2.line(canvas, (0, 0), (300, 300), green)  # draw a green line from corner to corner
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)  # last parameter makes thickness 3px
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.rectangle(canvas, (10, 10), (60, 60), green)  # rectangle method with start and end points
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)  # last parameter is thickness
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle (canvas, (200, 50), (225, 125), blue, -1)  # negative thickness means filled in
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
canvas = np.zeros((300, 300, 3), dtype="uint8")   # reinitialze for blank canvas
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)  # make center by halving dimensions of canvas
white = (255, 255, 255)

for r in range(0, 176, 25):  # ends at 150, range is exclusive
    cv2.circle(canvas, (centerX, centerY), r, white)  # third argument, r, is radius

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
for i in range(0, 25):
    radius = np.random.randint(5, high = 200)
    color = np.random.randint(0, high = 256, size = (3,)).tolist()   # size 3 gives 3 values
    pt = np.random.randint(0, high = 300, size =(2,))

    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
