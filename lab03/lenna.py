import cv2
import math

# 1. Load the Lenna image
image = cv2.imread("Lenna.png")

# 2. Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Save the grayscale image
cv2.imwrite("GsLenna.png", gray_image)

# 4. Find the highest valued pixel value using OpenCV function
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray_image)
print("Highest pixel value using OpenCV function:", max_val)

# 5. Find the highest valued pixel value without using OpenCV function
max_val_manual = 0
for row in gray_image:
    for pixel in row:
        if pixel > max_val_manual:
            max_val_manual = pixel
print("Highest pixel value without OpenCV function:", max_val_manual)

# 6. Find the lowest valued pixel value without using OpenCV function
min_val_manual = 255
for row in gray_image:
    for pixel in row:
        if pixel < min_val_manual:
            min_val_manual = pixel
print("Lowest pixel value without OpenCV function:", min_val_manual)

# 7. Count the total occurrences of lowest valued pixels in the image
lowest_pixel_count = sum(
    sum(pixel == min_val_manual for pixel in row) for row in gray_image
)
print("Total occurrences of lowest valued pixels:", lowest_pixel_count)


print("Coordinates of highest valued pixel using OpenCV function:", max_loc)

# Find the lowest valued pixel coordinates without using OpenCV function
min_val_manual = 255
min_loc_manual = None
for y, row in enumerate(gray_image):
    for x, pixel in enumerate(row):
        if pixel < min_val_manual:
            min_val_manual = pixel
            min_loc_manual = (x, y)
print("Coordinates of lowest valued pixel without OpenCV function:", min_loc_manual)

# Calculate the Euclidean distance between the two selected pixels using OpenCV function
distance_opencv = cv2.norm(max_loc, min_loc_manual, cv2.NORM_L2)
print("Euclidean distance between pixels using OpenCV function:", distance_opencv)

# Calculate the Euclidean distance between the two selected pixels manually
x1, y1 = max_loc
x2, y2 = min_loc_manual
distance_manual = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Euclidean distance between pixels without OpenCV function:", distance_manual)
