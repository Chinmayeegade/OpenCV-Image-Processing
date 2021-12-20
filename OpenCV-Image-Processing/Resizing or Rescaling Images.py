import cv2
image = cv2.imread("img_1.png")
cv2.imshow("Squares", image)
new_width = 600
new_height = 400
new_points = (new_width, new_height)
resized= cv2.resize(image, new_points, interpolation= cv2.INTER_LINEAR)
cv2.imshow("Squares_New", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

