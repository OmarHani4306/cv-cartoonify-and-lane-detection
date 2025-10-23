import os, cv2

img = cv2.imread(os.path.join(os.path.dirname(__file__), 'road.png'))

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()