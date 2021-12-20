import cv2
import numpy
#Creating a plain canvas
canvas = numpy.zeros((250,250,3),dtype="uint8")
#Height = 250, Width = 250, Broadcast Colors = 3
cv2.circle(canvas,(125,125),75,(255,0,0),-1)
#(canvas,(center points),radius,(color:BGR),thickness)
#Object is completely filled when thickness = -1
cv2.putText(canvas,"Circle",(30,30),cv2.FONT_HERSHEY_TRIPLEX,1.0,(0,225,0),2)
#(canvas,"text",(position),font,fontscale,(color:BGR),thickness)
cv2.imshow("Black Screen",canvas)
#Changing the color of the screen
canvas[:] = 0,225,0     #BGR (Blue,Green,Red)
#The square bracket can input coordinates for the canvas to be selectively colored [a:b,c:d]
cv2.rectangle(canvas,(50,50),(200,200),(255,0,0),5)
#(canvas,(point1),(point2),(color:BGR),thickness)
cv2.line(canvas,(0,0),(250,250),(0,0,255),1)
cv2.line(canvas,(0,250),(250,0),(0,0,255),1)
#(canvas,(point1),(point2),(color:BGR),thickness)
cv2.imshow("Green Screen",canvas)
cv2.waitKey(0)

#Shapes & text can be overwritten on images by using img = cv.imread("img_1.png") in place of canvas