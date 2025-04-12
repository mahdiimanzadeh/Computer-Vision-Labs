import cv2
import numpy as np
import matplotlib.pyplot as plt

def invert_image(image_path):
    # Load image in grayscale
    I = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if I is None:
        print("Error: Unable to load image.")
        return
    
    # Invert image colors
    I_inverted = 255 - I
    
    # Plot original and inverted images
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Show original image
    axes[0].imshow(I, cmap='gray', vmin=0, vmax=255)
    axes[0].set_title("Original Image")
    axes[0].axis("off")
    
    # Show inverted image
    axes[1].imshow(I_inverted, cmap='gray', vmin=0, vmax=255)
    axes[1].set_title("Inverted Image")
    axes[1].axis("off")
    
    plt.tight_layout()
    plt.show()

# Example usage
image_path = 'C:\\Users\\mandegar\\Documents\\courses\\Computer Vision\\LAB3\\cv-lab3\\inversion.png'  # Replace with your image file
invert_image(image_path)


'''
● Where can we Use grayscale image inversion? medical imaging
● Does inverting a grayscale image affect its histogram? why or why not?
 What Happens When You Invert an Image?
Inverting a grayscale image means replacing each pixel intensity I(x, y) with its complement:
𝐼′=255−𝐼

Dark pixels (close to 0) become bright (close to 255).
Bright pixels (close to 255) become dark (close to 0).
Mid-range pixels (e.g., 127) stay around the same.
'''