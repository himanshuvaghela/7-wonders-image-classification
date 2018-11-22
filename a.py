import cv2
import os
import sys

name = sys.argv[1]
img = os.listdir(name)
sorted(img)
counter = 0
for i in img:
	n=name+"/"+i
	print(n)
	im = cv2.imread(name+"/"+i)
	cv2.imwrite("image"+str(counter)+".jpg",im)
	print("image"+str(counter)+".jpg")
	counter+=1
