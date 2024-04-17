import cv2 as cv
import numpy as np

colored_image = cv.imread("image.jpg")
cv.imshow("Man and Women", colored_image)
cv.waitKey(0)
image_height, image_width, _ = colored_image.shape
image_mode = colored_image.dtype

greyscale_image = cv.cvtColor(colored_image, cv.COLOR_BGR2GRAY)

square_section = colored_image[0:100, 0:100]
cv.imwrite("lab1.jpg", square_section)

with open("properties.txt", "w") as f:
    f.write(f"Image Width: {image_width}\n")
    f.write(f"Image Height: {image_height}\n")
    f.write(f"Image Mode: {image_mode}\n")

white_pixel_count = np.sum(greyscale_image == 255)

greyscale_image[greyscale_image == 255] = 0

cv.imwrite("black_image.jpg", greyscale_image)
print(f"White space count = {white_pixel_count}")
print("Tasks completed successfully!")
