import cv2
import numpy as np
import matplotlib.pyplot as plt


# Load image in grayscale and convert to float [0,1]
I = cv2.imread(r"C:\Users\mandegar\Documents\courses\Computer Vision\LAB4\lenna.png", cv2.IMREAD_GRAYSCALE)
I = I.astype(np.float32) / 255.0  # shape: (H, W)

# Function to add Gaussian noise
def add_gaussian_noise(img, sigma=0.05):
    noise = np.random.randn(*img.shape) * sigma
    # Example: noise = np.random.randn(*img.shape) * sigma
    # TODO: Add the noise to the input image.
    noisy_img = img + noise
    # TODO: Clip the resulting values to ensure they remain in the [0,1] range.
    noisy_img = np.clip(noisy_img, 0.0, 1.0)
    return noisy_img

# Function to add salt-and-pepper noise
def add_salt_pepper_noise(img, p=0.2):
    # TODO: Create a copy of the image to modify.
    noisy_img = img.copy()
    # TODO: Determine the number of pixels to alter based on the given p
    num_pixles = img.size
    # TODO: Randomly choose indices for salt (set to 1.0) and pepper (set to 0.0).
   
    num_salt = int(num_pixles *p/2 )
    num_pepper = int(num_pixles *p/2 )
    
    # Add Salt noise (white pixels)
    # Generate random coordinates
    salt_coords = [np.random.randint(0, i-1, num_salt) for i in img.shape]
    noisy_img[salt_coords[0], salt_coords[1]] = 1.0
    
    # Add Pepper noise (black pixels)
    # Generate random coordinates
    pepper_coords = [np.random.randint(0, i-1, num_pepper) for i in img.shape]
    noisy_img[pepper_coords[0], pepper_coords[1]] = 0.0
    
    return noisy_img

# Generate noisy images using your implementations
gauss_noisy = add_gaussian_noise(I, sigma=0.1)
sp_noisy = add_salt_pepper_noise(I)

# Convert the noisy images back to uint8 for saving or displaying
cv2.imwrite(r"C:\Users\mandegar\Documents\courses\Computer Vision\LAB4\noisy_gaussian.png", (gauss_noisy * 255).astype(np.uint8))
cv2.imwrite(r"C:\Users\mandegar\Documents\courses\Computer Vision\LAB4\noisy_saltpepper.png", (sp_noisy * 255).astype(np.uint8))


def analyze_noise(original, noisy, noise_type, param_value):
    noise = noisy - original
    plt.figure(figsize=(12,4))
    
    plt.subplot(131)
    plt.imshow(noisy, cmap='gray')
    plt.title(f"{noise_type} noise (param={param_value})")
    
    plt.subplot(132)
    plt.hist(noise.ravel(), bins=50, density=True)
    plt.title("Noise distribution")
    
    if noise_type == "Gaussian":
        x = np.linspace(-3*param_value, 3*param_value, 100)
        plt.plot(x, 1/(param_value*np.sqrt(2*np.pi)) * np.exp(-0.5*(x/param_value)**2), 'r')
    
    plt.subplot(133)
    plt.hist(original.ravel(), bins=50, alpha=0.5, label='Original')
    plt.hist(noisy.ravel(), bins=50, alpha=0.5, label='Noisy')
    plt.legend()
    plt.title("Pixel value histograms")
    
    plt.tight_layout()
    plt.show()

gauss_noisy = add_gaussian_noise(I, 0.1)
analyze_noise(I, gauss_noisy, "Gaussian", 0.1)

sp_noisy = add_salt_pepper_noise(I, 0.05)
analyze_noise(I, sp_noisy, "Salt-and-Pepper", 0.05)