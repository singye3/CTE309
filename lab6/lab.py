import cv2
from operation import *

lenna_image = cv2.imread("Lenna.png")
gray_lenna = cv2.cvtColor(lenna_image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("GsLenna.jpg", gray_lenna)

ori_and_gray_image(lenna_image,gray_lenna)

brightness_histrogram(gray_lenna=gray_lenna)

linear_corrected = linear_correction(gray_lenna)


# Plot the brightness histogram after linear correction
hist_comparison(gray_lenna,linear_corrected)

original_and_corrected(gray_lenna,linear_corrected)

apply_gamma_correction(gray_lenna)



