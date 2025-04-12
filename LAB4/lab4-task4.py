import numpy as np
import cv2

# Load the noisy image in grayscale and normalize to [0,1]
I = cv2.imread(r"C:\Users\mandegar\Documents\courses\Computer Vision\LAB4\noisy_gaussian.png", cv2.IMREAD_GRAYSCALE).astype(np.float32) / 255.0

m = 5  # Filter size (try different values, e.g., 3, 13, 21)

# === Create a 1D Gaussian kernel using cv2.getGaussianKernel ===
# Use sigma=0 to let OpenCV choose sigma automatically.
g1d = cv2.getGaussianKernel(m, sigma=0)

# === Create a 2D Gaussian kernel by taking the outer product of g1d with its transpose ===
Gkernel = g1d * g1d.T

print("1D Gaussian kernel (m=%d):" % m, g1d.flatten())
print("2D Gaussian kernel sum:", Gkernel.sum())

# === Apply the Gaussian filter using cv2.filter2D (or cv2.GaussianBlur) ===
J_gauss = cv2.filter2D(I, -1, Gkernel)

# === Convert the result to uint8 and save or display it ===
# Convert back to 0-255 range and uint8 type
J_uint8 = (J_gauss * 255).astype(np.uint8)

# Save the result
cv2.imwrite('gaussian_filtered.png', J_uint8)

# Display results
cv2.imshow('Original Image', I)
cv2.imshow('Gaussian Filtered Image', J_gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Comparison: 13×13 Gaussian vs. 13×13 Box Filter
m = 13
# Gaussian
gauss_blur = cv2.GaussianBlur(I, (m,m), sigmaX=0)  # Default σ
# Box filter
box_blur = cv2.blur(I, (m,m))
# Display
cv2.imshow('Gaussian (13×13)', gauss_blur)
cv2.imshow('Box (13×13)', box_blur)
cv2.waitKey(0)

'''
1D Gaussian Kernel:
Symmetric, centered, and sums to 1.
Larger m → OpenCV increases σ → stronger blur.

Gaussian vs. Box (13×13):
Gaussian outperforms in noise reduction and detail preservation.
Box blurs uniformly, losing edges and creating artifacts.
'''