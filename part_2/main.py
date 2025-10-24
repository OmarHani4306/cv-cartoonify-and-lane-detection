import os, cv2
import numpy as np

k_median_size = 3

img = cv2.imread(os.path.join(os.path.dirname(__file__), 'road.png'))
cv2.imshow('img', img)

img_median_blur = cv2.medianBlur(img, k_median_size)
# cv2.imshow('img_median_blur', img_median_blur)

img_edge = cv2.Canny(img, 100, 300)
# cv2.imshow('img_edge', img_edge)

pts = np.array([[0, img_edge.shape[0]-3], [0,124], [20,124], [16,92], [172,88], [261,img_edge.shape[0]-3]], dtype=np.int32)
mask = np.zeros(img_edge.shape[:2], dtype=np.uint8)
poly = cv2.fillPoly(mask, [pts], 255)  # white polygon on black mask
img_roi = cv2.bitwise_and(img_edge, img_edge, mask=mask)
cv2.imshow("img_roi", img_roi)
# cv2.imshow("poly", poly)

filename = "img_roi.jpg"
cv2.imwrite(filename, img_roi)


cv2.waitKey(0)
cv2.destroyAllWindows()