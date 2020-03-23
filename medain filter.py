import numpy as np
import cv2

from matplotlib import pyplot as plt
random_matrix_array = np.random.randint(1, 1550, size=(6, 4))
median = cv2.medianBlur(random_matrix_array,3)


plt.imshow(median)
plt.show()
print('random matrix = ',random_matrix_array)
print('---------------------------------------------------------------------------------------------/n')
print('after using filtering the pixel size is nearly same /n')
print(median)
