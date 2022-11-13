import cv2
import matplotlib.pyplot as plt

import os
os.chdir("C:/git/WKIT/Test/")

# 이미지 보여주기
image_path = './Data/Image/02.jpg'
im = cv2.imread(image_path) # 이미지 읽기


fix_img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

# 새창에서 띄우기
# cv2.imshow('fix_img', im)
# cv2.waitKey(0)

plt.imshow(fix_img)
plt.axis('off')
print(plt.show())