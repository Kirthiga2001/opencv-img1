import cv2
import  numpy as np
i=cv2.imread('lena.jpg',1)
k=np.ones((5,5),np.uint8)
b=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
blur=cv2.blur(i,(7,7),0) #(num,num) num>> blur>>
blur1=cv2.blur(i,(7,7),1)
blur2=cv2.blur(i,(7,7),10)
icanny=cv2.Canny(i,150,100) #more the num less the edges
idilation=cv2.dilate(icanny,k,iterations=3) #increase thickness
ierode=cv2.erode(idilation,k,iterations=3)# decrease thivkness
#cv2.imshow("try",i)
#cv2.imshow("black and white",b)
cv2.imshow("original",idilation)
cv2.imshow("blur1",ierode)
cv2.imshow("canny",icanny)
cv2.waitKey(6000)
cv2.destroyAllWindows()
#cv2.imwrite("lc.png",i) #copy
print("Done")