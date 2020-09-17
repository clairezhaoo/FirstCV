import numpy as np
import cv2

rectangle = np.zeros((300, 300), dtype = "uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)  # rectangle inside rect
cv2.imshow("Rectangle", rectangle)
cv2.waitKey(0)
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)  # circle inside circle
cv2.imshow("Circle", circle)
bitwiseAnd = cv2.bitwise_and(rectangle, circle) # true: both pixels greater than 0
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(rectangle, circle)  # true: one of pixels is greater than 0
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(rectangle, circle) # true: only one of pixels is greater than 0
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(circle)  # inverts the "on" and "off" pixels
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)
