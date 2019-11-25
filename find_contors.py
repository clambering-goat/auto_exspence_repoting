import numpy as np
import cv2

import matplotlib.pyplot as plt
img = cv2.imread('teast_img_1.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)


light_orange = (90, 80, 22)
dark_orange = (122, 255, 209)

mask = cv2.inRange(imgray, light_orange, dark_orange)

contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



temp=[]
for q in contours:
    temp.append(cv2.contourArea(q))
    if cv2.contourArea(q)>5000:
        cv2.drawContours(img, q, -1, (0,255,0), 10)
print(max(temp))

plt.imshow(img)
plt.show()
