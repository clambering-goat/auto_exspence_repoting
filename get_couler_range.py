import cv2

file_dir = "./teast_img_1.jpg"
# file_dir="teast_2.PNG"
img = cv2.imread(file_dir)

hsv_nemo = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

list_vaule_r = []
list_vaule_g = []
list_vaule_b = []
for y in range(1340, 3815):
    for x in range(960, 1700):
        list_vaule_r.append(hsv_nemo[y][x][0])
        list_vaule_g.append(hsv_nemo[y][x][1])
        list_vaule_b.append(hsv_nemo[y][x][2])

print(max(list_vaule_r))
print(min(list_vaule_r))
print("----------------")
print(max(list_vaule_g))
print(min(list_vaule_g))
print("----------------")
print(max(list_vaule_b))
print(min(list_vaule_b))
print("hi")