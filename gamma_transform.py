# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 23:11:58 2020

@author: Avinash
"""

import numpy as np
import cv2

img = cv2.imread("image.jpg",0)

gamma = 0.2
img_gama2 = np.power(img,gamma)

gamma = 3
img_gama3 = np.power(img, gamma)

gamma = 4
img_gama4 = np.power(img, gamma)

cv2.imshow("Gamma=2",img_gama2)
cv2.imshow("Gamma=2",img_gama3)
cv2.imshow("Gamma=2",img_gama4)

cv2.waitKey(0)
cv2.destroyAllWindows()