import numpy as np
import math
import cv2


def rotate(image_path,rotation_amount_degree = 45):
    # Read the image using imageio
    img = cv2.imread(image_path)

    # Convert rotation amount to radians
    rotation_amount_rad = rotation_amount_degree * np.pi / 180.0

    # Get dimension info
    height, width, num_channels = img.shape

    # Create output image, for worst case size (45 degree)
    max_len = int(math.sqrt(height * height + width * width))
    rotated_image = np.zeros((max_len, max_len, num_channels))

    rotated_height, rotated_width, _ = rotated_image.shape
    mid_row = int((rotated_height + 1) / 2)
    mid_col = int((rotated_width + 1) / 2)

    # For each pixel in output image, find which pixel it corresponds to in the input image
    for r in range(rotated_height):
        for c in range(rotated_width):
            # Apply rotation matrix, the other way
            y = (r - mid_col) * math.cos(rotation_amount_rad) + (c - mid_row) * math.sin(rotation_amount_rad)
            x = -(r - mid_col) * math.sin(rotation_amount_rad) + (c - mid_row) * math.cos(rotation_amount_rad)

            # Add offset
            y += mid_col
            x += mid_row

            # Get nearest index (a better way is linear interpolation)
            x = round(x)
            y = round(y)

            # Check if x/y corresponds to a valid pixel in input image
            if (x >= 0 and y >= 0 and x < width and y < height):
                rotated_image[r][c][:] = img[y][x][:]

    # Save output image using cv2
    output_image_path = "rotated_image.png"
    cv2.imwrite(output_image_path, rotated_image.astype("uint8"))

    return rotated_image.astype("uint8")