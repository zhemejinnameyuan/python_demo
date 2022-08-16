
from hyperlpr import *

import cv2

# image = cv2.imread("lanpai.jpeg")
image = cv2.imread("lvpai.jpeg")

result = HyperLPR_plate_recognition(image)
print(result)