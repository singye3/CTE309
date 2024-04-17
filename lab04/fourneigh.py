import cv2
import random

image = cv2.imread("img.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


with open("neighbours.txt", "w") as f:
    for _ in range(10):
        y = random.randint(0, gray_image.shape[1] - 1)
        x = random.randint(0, gray_image.shape[0] - 1)

        neighbors = []

        neighbors.append({gray_image[x, y - 1]: (x, y - 1)})
        neighbors.append({gray_image[x, y + 1]: (x, y + 1)})
        neighbors.append({gray_image[x - 1, y]: (x - 1, y)})
        neighbors.append({gray_image[x + 1, y]: (x + 1, y)})

        f.write(f"Pixel location: ({x}, {y})\n")
        f.write("Neighbors:\n")
        for neighbor in neighbors:
            f.write(f"{neighbor}\n")
        f.write("\n")
