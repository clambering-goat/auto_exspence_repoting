import cv2
import matplotlib.pyplot as plt

file_dir = "./teast_img_1.jpg"
# file_dir="teast_2.PNG"
img = cv2.imread(file_dir)

hsv_nemo = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
light_orange = (200, 200, 220)
dark_orange = (255, 255, 255)

mask = cv2.inRange(hsv_nemo, light_orange, dark_orange)
result = cv2.bitwise_and(img, img, mask=mask)

#plt.subplot(1, 2, 1)
plt.imshow(result, cmap="gray")
#plt.subplot(1, 2, 2)
#plt.imshow(hsv_nemo)
plt.show()
