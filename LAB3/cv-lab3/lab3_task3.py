import cv2
import numpy as np
import matplotlib.pyplot as plt

I = cv2.imread("C:\\Users\\mandegar\\Documents\\courses\\Computer Vision\\LAB3\\cv-lab3\\task3p1.png", cv2.IMREAD_GRAYSCALE)

levels = 256

def calc_hist(I, levels):
    hist = np.zeros(levels, dtype=np.int32)  # Initialize histogram array
    for pixel in I.ravel():  # Flatten the image array
        hist[pixel] += 1  # Count occurrences of each intensity level
    return hist

# Manually compute the CDF
def calc_cdf(hist):
    cdf = np.cumsum(hist)  # Cumulative sum of the histogram
    cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())  # Normalize to range [0,255]
    return cdf_normalized.astype(np.uint8)

# Compute histogram and CDF
hist = calc_hist(I, levels)
cdf = calc_cdf(hist)

# Create a mapping from original to equalized intensities
mapping = np.zeros(levels, dtype=np.uint8)
for i in range(levels):
    mapping[i] = cdf[i]  # Use CDF as the mapping function

# Replace intensities based on mapping
equalized_image = mapping[I]

# Compute histogram and CDF of the equalized image
equalized_image_hist = calc_hist(equalized_image, levels)
equalized_image_cdf = calc_cdf(equalized_image_hist)

fig = plt.figure(figsize= (16, 8))
fig.add_subplot(2,3,1)
plt.imshow(I, cmap='gray')
plt.title('pasargadae')
plt.axis('off')

fig.add_subplot(2,3,2)
plt.plot(hist)
plt.title('Source histogram')

fig.add_subplot(2,3,3)
plt.plot(cdf)
plt.title('Source CDF')

fig.add_subplot(2,3,4)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized image')
plt.axis('off')

fig.add_subplot(2,3,5)
plt.plot(equalized_image_hist)
plt.title('Equalized histogram')


fig.add_subplot(2,3,6)
plt.plot(equalized_image_cdf)
plt.title('Equalized CDF')

plt.show()


'''
If two images have the same histogram, does it mean they look identical? why
or why not?
❌ No, two images with the same histogram do NOT necessarily look identical.
✅ The histogram only captures the frequency of intensity values but does not store spatial information (where the pixels are located).

● If two images have the same histogram before equalization, will their
equalized versions also be identical? why or why not?
✅ Yes, if two images have identical histograms before equalization, their equalized versions will also be identical.
🔹 Why?
Histogram equalization is a global operation that applies the same transformation to all pixels based on the Cumulative Distribution Function (CDF).

● In what real-world applications might comparing histograms be useful? What
are the limitations of using histograms for image comparison?
✅ 2. Medical Image Processing (X-ray, MRI, CT Scan Analysis)
Histogram equalization helps enhance contrast in medical images.
Doctors compare histograms to detect anomalies (tumors, fractures, etc.).

❌ Sensitive to Brightness Changes
If the lighting changes (e.g., day vs. night), histograms may differ even if the scene is the same.
Solution: Use normalized histograms to reduce this effect.
'''