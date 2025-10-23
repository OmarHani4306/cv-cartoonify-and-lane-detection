import cv2, os

img = cv2.imread(os.path.join(os.getcwd(), 'part_1', 'tarboosh.jpeg'))

cv2.imshow('img', img)
cv2.waitKey(0)

