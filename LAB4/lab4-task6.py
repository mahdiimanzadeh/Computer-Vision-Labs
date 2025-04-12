import cv2
import numpy as np

# Initialize parameters
m = 3  # Kernel size (odd)
sigma_color = 50  # Bilateral filter color sigma
noise_sigma = 0.05  # Gaussian noise standard deviation
current_filter = 'n'  # Start with no filter
img = cv2.imread(r"C:\Users\mandegar\Documents\courses\Computer Vision\LAB4\lenna.png")  # Load test image
img = img.astype(np.float32) / 255.0  # Normalize to [0,1]

# Create window
cv2.namedWindow('Denoising Demo')

while True:
    # Add noise
    noise = np.random.randn(*img.shape) * noise_sigma
    noisy_img = np.clip(img + noise, 0, 1)
    
    # Apply selected filter
    if current_filter == 'n':
        filtered = noisy_img
    elif current_filter == 'b':
        filtered = cv2.blur(noisy_img, (m, m))
    elif current_filter == 'g':
        filtered = cv2.GaussianBlur(noisy_img, (m, m), 0)
    elif current_filter == 'm':
        filtered = cv2.medianBlur((noisy_img * 255).astype(np.uint8), m).astype(np.float32) / 255.0
    elif current_filter == 'l':
        filtered = cv2.bilateralFilter((noisy_img * 255).astype(np.uint8), m, sigma_color, sigma_color)
        filtered = filtered.astype(np.float32) / 255.0
    
    # Display
    cv2.imshow('Denoising Demo', filtered)
    
    # Print status
    print(f"\rFilter: {current_filter} | Kernel: {m}x{m} | σ_color: {sigma_color} | Noise σ: {noise_sigma:.3f}", end='')
    
    # Key handling
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
    elif k == ord('n'):
        current_filter = 'n'
    elif k == ord('b'):
        current_filter = 'b'
    elif k == ord('g'):
        current_filter = 'g'
    elif k == ord('m'):
        current_filter = 'm'
    elif k == ord('l'):
        current_filter = 'l'
    elif k == ord('+'):
        m = min(m + 2, 31)  # Max kernel size 31
    elif k == ord('-'):
        m = max(m - 2, 3)  # Min kernel size 3
    elif k == ord('.'):
        sigma_color = min(sigma_color + 5, 150)
    elif k == ord(','):
        sigma_color = max(sigma_color - 5, 5)
    elif k == ord('u'):
        noise_sigma = min(noise_sigma + 0.01, 0.2)
    elif k == ord('d'):
        noise_sigma = max(noise_sigma - 0.01, 0.01)

cv2.destroyAllWindows()