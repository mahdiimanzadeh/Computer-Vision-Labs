import cv2
import numpy as np
import time

# Load color image and normalize to [0, 1] range
I = cv2.imread(r"C:\Users\mandegar\Documents\courses\Computer Vision\LAB4\lenna.png").astype(np.float32) / 255.0

# Add Gaussian noise (5% of pixel intensity range)
noise = np.random.randn(*I.shape) * 0.05
noisy_color = np.clip(I + noise, 0.0, 1.0)

# Convert back to 8-bit for OpenCV processing
noisy_color_uint8 = (noisy_color * 255).astype(np.uint8)

# Bilateral filter parameters
d = 9  # Diameter of pixel neighborhood (0 means automatic from sigmaSpace)
sigma_color = 25  # Larger value means more colors will be mixed together
sigma_space = 15  # Larger value means farther pixels will influence each other

# Apply bilateral filter
denoised_bilateral = cv2.bilateralFilter(
    noisy_color_uint8,
    d=d,
    sigmaColor=sigma_color,
    sigmaSpace=sigma_space
)

# Save and show results
cv2.imwrite('noisy_image.png', noisy_color_uint8)
cv2.imwrite('denoised_bilateral.png', denoised_bilateral)

# Display comparison
cv2.imshow('Noisy Image', noisy_color_uint8)
cv2.imshow('Bilateral Filtered', denoised_bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
High Sigma Color : Allows mixing of more dissimilar colors
High Sigma Space : Considers pixels from a much larger area
'''


# Gaussian blur timing
start = time.time()
gauss = cv2.GaussianBlur(I, (15,15), sigmaX=5)
print(f"Gaussian: {1000*(time.time() - start):.2f} ms")

# Bilateral filter timing
start = time.time()
bilateral = cv2.bilateralFilter(noisy_color_uint8, d=15, sigmaColor=50, sigmaSpace=5)
print(f"Bilateral: {1000*(time.time() - start):.2f} ms")