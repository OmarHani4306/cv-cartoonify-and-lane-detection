import os, cv2
import numpy as np

k_median_size = 3

img = cv2.imread(os.path.join(os.path.dirname(__file__), 'road.png'))
cv2.imshow('img', img)

img_median_blur = cv2.medianBlur(img, k_median_size)
# cv2.imshow('img_median_blur', img_median_blur)

img_edge = cv2.Canny(img, 100, 300)
cv2.imshow('img_edge', img_edge)

# roi = cv2.selectROI(img_edge)
# print(roi)
#
# img_cropped = img_edge[int(roi[1]):int(roi[1]+roi[3]),
# 			int(roi[0]):int(roi[0]+roi[2])]

# cv2.imshow("img_cropped", img_cropped)


# (0, 124, 264, 61) -> bottom
# (16, 92, 114, 30) -> top-left
# (155, 89, 17, 13) -> top-right
# (153, 99, 46, 27) -> middle-right

# pts: Nx2 array of (x, y) polygon vertices
pts = np.array([[0, img_edge.shape[0]], [0,124], [20,124], [16,92], [172,88], [261,img_edge.shape[0]]], dtype=np.int32)
mask = np.zeros(img_edge.shape[:2], dtype=np.uint8)
poly = cv2.fillPoly(mask, [pts], 255)  # white polygon on black mask
img_roi = cv2.bitwise_and(img_edge, img_edge, mask=mask)
cv2.imshow("img_roi", img_roi)
cv2.imshow("poly", poly)

cv2.waitKey(0)
cv2.destroyAllWindows()
