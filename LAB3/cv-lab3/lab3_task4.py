import cv2
import numpy as np
import matplotlib.pyplot as plt

def classify_image(image_path):
    # Load image in grayscale
    I = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if I is None:
        print("Error: Unable to load image.")
        return
    
    # Compute histogram
    hist, bins = np.histogram(I.ravel(), 256, [0,256])
    
    # Compute mean intensity and standard deviation
    mean_intensity = np.mean(I)
    std_dev = np.std(I)
    
    # Compute proportion of dark and bright pixels
    dark_pixels = np.sum(hist[:50]) / I.size  # Pixels with intensity < 50
    bright_pixels = np.sum(hist[200:]) / I.size  # Pixels with intensity > 200
    
    # Classification logic
    category = ""
    if mean_intensity < 50 and dark_pixels > 0.5:
        category = "Underexposed (Too Dark)"
    elif mean_intensity > 200 and bright_pixels > 0.5:
        category = "Overexposed (Too Bright)"
    elif std_dev < 30:
        category = "Low Contrast (Faded Image)"
    else:
        category = "Well-Balanced (Good Exposure & Contrast)"
    
    # Print classification result
    print(f"Image Classification: {category}")
    print(f"Mean Intensity: {mean_intensity:.2f}, Standard Deviation: {std_dev:.2f}")
    print(f"Dark Pixels: {dark_pixels:.2%}, Bright Pixels: {bright_pixels:.2%}")
    
    # Plot image and histogram
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Show image
    axes[0].imshow(I, cmap='gray', vmin=0, vmax=255)
    axes[0].set_title("Grayscale Image")
    axes[0].axis("off")
    
    # Show histogram
    axes[1].hist(I.ravel(), bins=256, range=[0,256], color='gray', alpha=0.7)
    axes[1].axvline(mean_intensity, color='red', linestyle='dashed', label=f'Mean: {mean_intensity:.2f}')
    axes[1].set_title("Histogram of Image")
    axes[1].set_xlabel("Pixel Intensity")
    axes[1].set_ylabel("Frequency")
    axes[1].legend()
    
    plt.tight_layout()
    plt.show()

# Example usage
image_path = 'C:\\Users\\mandegar\\Documents\\courses\\Computer Vision\\LAB3\\cv-lab3\\pasargadae.jpg'  # Replace with your image file
classify_image(image_path)



'''
1. What Threshold Values Should Be Chosen for Categorization?

2. How Does Histogram Distribution Help in Classification?
A histogram represents the distribution of pixel intensities. Different histogram shapes correspond to different image types:
Underexposed (Dark Image)
Histogram peaks on the left (low intensity values).
Most pixel values are near 0-50.
Overexposed (Bright Image)
Histogram peaks on the right (high intensity values).
Most pixel values are near 200-255.
Low Contrast
Histogram is narrow (pixel values are clustered in a small range).
No strong shadows or highlights.
Well-Balanced
Histogram is spread across all intensity values.
Good distribution of dark, midtone, and bright pixels.


3. How does the standard deviation (std_dev) of pixel intensities in an image help in determining its contrast level?
Standard Deviation (np.std(I)) measures pixel intensity spread.
Higher std_dev → Pixel values are widely spread → High contrast (clear difference between dark and bright areas).
Lower std_dev → Pixel values are clustered → Low contrast (faded or washed-out appearance).

'''