import cv2
import matplotlib.pyplot as plt
import numpy as np


def ori_and_gray_image(original,gray_image):
    _, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Display the original grayscale image in the first subplot
    axs[0].imshow(original, cmap='gray')
    axs[0].set_title('Original Image')
    axs[0].axis('off') # Hide axes

    # Display the linear corrected image in the second subplot
    axs[1].imshow(gray_image, cmap='gray')
    axs[1].set_title('Gray Scale Image')
    axs[1].axis('off') # Hide axes

    plt.tight_layout()
    plt.show()

def brightness_histrogram(gray_lenna):
    plt.hist(gray_lenna.flatten(), bins=256, color="r")
    plt.title("Brightness Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.show()

def linear_correction(gray_lenna):

    linear_corrected = []
    min_val = min(gray_lenna.flatten())
    max_val = max(gray_lenna.flatten())
    for input in gray_lenna.flat:
        linear_corrected.append((input - min_val) * (255 / (max_val - min_val)))
    
    return linear_corrected

def hist_comparison(gray_lenna,linear_corrected):
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot the original brightness histogram
    ax.hist(gray_lenna.flatten(), bins=256, color="r", alpha=0.5, label="Original")
    ax.hist(linear_corrected, bins=256, color="b", alpha=0.5, label="Linear Corrected")

    # Set the title, labels, and legend
    ax.set_title("Brightness Histogram Comparison")
    ax.set_xlabel("Pixel Value")
    ax.set_ylabel("Frequency")
    ax.legend()

    plt.savefig('histogram_comparison.png')
    plt.show()

def original_and_corrected(gray_lenna,linear_corrected):
    
    linear_corrected_array = np.array(linear_corrected, dtype=np.uint8)
    linear_corrected_array = linear_corrected_array.reshape(gray_lenna.shape)

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Display the original grayscale image in the first subplot
    axs[0].imshow(gray_lenna, cmap='gray')
    axs[0].set_title('Original Image')
    axs[0].axis('off') # Hide axes

    # Display the linear corrected image in the second subplot
    axs[1].imshow(linear_corrected_array, cmap='gray')
    axs[1].set_title('Linear Corrected Image')
    axs[1].axis('off') # Hide axes
    plt.tight_layout()

    # Show the plot
    plt.show()

#  Output = Input ^ (1 / gamma) : Display Channel Value
def gamma_correction(image, gamma):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)


def apply_gamma_correction(gs_lenna):

    gamma_values = [1, 0.5, 1.5, 2.2]
    fig, axs = plt.subplots(2, 2, figsize=(12, 5))


    for i, gamma in enumerate(gamma_values):
        row = i // 2
        col = i % 2
        gamma_corrected = gamma_correction(gs_lenna, gamma)
        axs[row, col].imshow(gamma_corrected, cmap='gray')
        axs[row, col].set_title(f'Gamma = {gamma}' if gamma != 1 else 'Original Image Without Gamma Correction')
        axs[row, col].axis('off')

    plt.tight_layout()
    plt.savefig('gamma_corrected_images.png')
    plt.show()

