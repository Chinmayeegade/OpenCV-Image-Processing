import cv2
import matplotlib.pyplot as plt
image = cv2.imread("img_2.png")
cv2.imshow("Image",image)
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV',hsv)
histogram = cv2.calcHist([hsv],[0],None,[256],[0,256])
#([list of images],channels,mask,Hist_size,range)
plt.figure()
plt.title("HSV Histogram")
plt.xlabel("Bins")
plt.ylabel("Pixels")
plt.plot(histogram)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)

#Similarly, various histograms can be created for all types of Images