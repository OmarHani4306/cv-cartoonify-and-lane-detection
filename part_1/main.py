import cv2, os

k_median_size = 3
k_laplace_size = 7
threshold_value = 120

# img = cv2.imread(os.path.join(os.getcwd(), 'part_1', 'tarboosh.jpeg'))
img = cv2.imread(os.path.join(os.getcwd(), 'tarboosh.jpeg'))
cv2.imshow('img', img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('img_gray', img_gray)

img_median_blur = cv2.medianBlur(img_gray, k_median_size)
# cv2.imshow('img_median_blur', img_median_blur)

img_edge = cv2.Laplacian(img_gray, cv2.CV_16S, ksize=k_laplace_size)
# cv2.imshow('img_edge', img_edge)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img_edge)
# img_edge_scaled = (((img_edge - min_val) / (2*max_val)) * 255).astype(int).astype(float)
img_edge_scaled = cv2.normalize(img_edge, None, alpha=0,beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_16S).astype(float)

ret, img_thresh = cv2.threshold(img_edge_scaled, threshold_value, 255, cv2.THRESH_BINARY)
cv2.imshow('img_thresh', img_thresh)

filename = "img_thresh.jpg"
cv2.imwrite(filename, img_thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

