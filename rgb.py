import numpy as np
import cv2


width, height = 800, 800

# Create blank image
img = np.zeros((height, width, 3), dtype=np.uint8)

# color the image
location = 0
shade = 20
n_shades = 255
for i in range(n_shades):
    img[0:height, location:location+width//n_shades, 1:3] = shade
    location += width//n_shades
    shade += 255//n_shades




# Save image
cv2.imwrite("my_img.png", img)






