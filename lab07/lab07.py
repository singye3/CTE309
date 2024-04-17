import cv2
import matplotlib.pyplot as plt
from rotate import rotate
from equalize_hist import equalizeHistogram

# Load the image
img = cv2.imread('cat.jpg')

# Convert to grayscale
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grey_cat.jpg', grey_img)

# Resize the image
resized_img = cv2.resize(grey_img, (200, 200))
cv2.imwrite('resized_cat.jpg', resized_img)

# Rotate the image by 90 degrees clockwise
rotated_img = cv2.rotate(resized_img,cv2.ROTATE_90_COUNTERCLOCKWISE)
# rotated_img = rotate('resized_cat.jpg', rotation_amount_degree=90)


# Convert rotated image to grayscale
# rotated_img = cv2.cvtColor(rotated_img, cv2.COLOR_BGR2GRAY)

# Perform histogram equalization
# equalized_img = cv2.equalizeHist(rotated_img_gray)
equalized_img = equalizeHistogram(rotated_img)
cv2.imwrite('equalized_image.jpg', equalized_img)

# Display the original and equalized images
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(grey_img, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(resized_img, cmap='gray')
plt.title('Resized Image')

plt.subplot(1, 3, 3)
plt.imshow(equalized_img, cmap='gray')
plt.title('Equalized Image')

plt.tight_layout()
plt.show()