import numpy as np
import cv2

# Load an image (using the noisy image from Task 1, or a clean image) in grayscale
I = cv2.imread("noisy_gaussian.png", cv2.IMREAD_GRAYSCALE)
I = I.astype(np.float32) / 255.0  # Normalize to [0,1]

m = 3 # Filter size (try 3, 5, 7, 11, etc.)

# === Create an m×m box filter kernel ===
# Use np.ones to create an array of ones and divide by (m*m) to normalize.
kernel = np.ones((m, m), dtype=np.float32) / (m * m)

# === Apply convolution to blur the image using cv2.filter2D ===
J = cv2.filter2D(I, -1, kernel)

# === Convert the result to uint8 and save or display it ===
# Convert back to 0-255 range and uint8 type
I_display = (I * 255).astype(np.uint8)  
J_display = (J * 255).astype(np.uint8)  
# Save the result
cv2.imwrite('mean_filtered.png', J_display)

# Optional: Display the results
combined = np.hstack((I_display, J_display))
cv2.imshow('Original (Left) vs Mean Filtered (Right)', combined)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
● Try m=3, 5, 9, 15. How does the choice of kernel size affect the output?
Larger kernel sizes increase blurring and noise removal but reduce sharpness and fine details.

● Why do we divide the kernel by ? What would happen if we don’t?
Normalization (Dividing by m²):
Ensures the sum of the kernel is 1, preserving the image’s brightness.
Without normalization, the output image may become too bright or even overflow (e.g., pixel values > 255).


● Use OpenCV’s cv2.blur(I, (m,m)) to perform the same operation. Confirm it
produces the same result as your filter2D approach.
Both methods produce identical results when using a normalized box filter.


● Suppose you apply two 3×3 mean filters sequentially (one after the other). Is the result
different from a single 5×5 filter?
h(combined()=h∗h

'''


# Method 2: cv2.blur
J_blur = cv2.blur(I, (m, m))

# Check if results are identical
difference = np.sum(np.abs(J - J_blur))
print("Difference:", difference)  # Should be ≈0 (identical)


# Two 3×3 filters
J_two_3x3 = cv2.filter2D(cv2.filter2D(I, -1, np.ones((3,3))/9), -1, np.ones((3,3))/9)

# One 5×5 filter
J_one_5x5 = cv2.filter2D(I, -1, np.ones((5,5))/25)

# Check the difference
difference = np.sum(np.abs(J_two_3x3 - J_one_5x5))
print("Difference:", difference)  # Small but non-zero