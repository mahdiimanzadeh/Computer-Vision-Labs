import cv2
import numpy as np

# Load the salt-and-pepper noisy image in grayscale
sp_noisy_img = cv2.imread(r"C:\Users\mandegar\Documents\courses\Computer Vision\LAB4\noisy_saltpepper.png", cv2.IMREAD_GRAYSCALE)

# Apply median filter with a 5x5 kernel
denoised_med5 = cv2.medianBlur(sp_noisy_img, ksize=5)

# Apply median filter with a 3x3 kernel for comparison
denoised_med3 = cv2.medianBlur(sp_noisy_img, ksize=3)

# Save the results
cv2.imwrite('denoised_median5.png', denoised_med5)
cv2.imwrite('denoised_median3.png', denoised_med3)

# Optional: Display the results
cv2.imshow('Original Noisy Image', sp_noisy_img)
cv2.imshow('Denoised (5x5)', denoised_med5)
cv2.imshow('Denoised (3x3)', denoised_med3)
cv2.waitKey(0)
cv2.destroyAllWindows()




# Apply Mean Filter To Compare
# Apply mean filter
denoised_mean3 = cv2.blur(sp_noisy_img, (3,3))  # 3×3 box filter
denoised_mean5 = cv2.blur(sp_noisy_img, (5,5))  # 5×5 box filter
# Compare median vs. mean filters
cv2.imshow('Median 3x3', denoised_med3)
cv2.imshow('Mean 3x3', denoised_mean3)
cv2.waitKey(0)
'''
Median Filter:
Discards outliers (noise pixels replaced by neighbors).
Preserves edges (sharp transitions remain).
Mean Filter:
Averages noise into the image (noise becomes "smudged").
Blurs edges (replaces pixels with local averages).
Visual Example:
Salt-and-pepper noise (black/white dots):
Median: Dots disappear.
Mean: Dots become gray smudges.
'''

'''
● Why is the median filter particularly suited for impulse noise?

Mathematical Reason:
For a neighborhood with one noisy pixel:
Sorted values: [10, 20, 30, 40, 255] (noise = 255).
Median = 30 (noise has no effect).
Mean = (10+20+30+40+255)/5 = 71 (noise corrupts the result).
Edge Preservation:
At edges, median selects a value from one side (not an average).
Example: Edge pixels [10, 10, 10, 200, 200] → Median = 10 (no blurring).
'''

