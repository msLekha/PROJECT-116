import cv2
#read image
img = cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(28,380),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
greyimg=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("img1",greyimg)
cv2.imshow("output",img)
cv2.waitKey(0)