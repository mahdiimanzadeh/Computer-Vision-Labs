import cv2
import numpy as np
from matplotlib import pyplot as plt

fname = 'C:\\Users\\mandegar\\Documents\\courses\\Computer Vision\\LAB3\\cv-lab3\\crayfish.jpg'
#fname = 'C:\\Users\\mandegar\\Documents\\courses\\Computer Vision\\LAB3\\cv-lab3\\office.jpg'

I = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)

f, axes = plt.subplots(2, 3)
# ---------------------------- Visualize Image I and it's Histogram ------------------------------

axes[0,0].imshow(I, 'gray', vmin=0, vmax=255)
axes[0,0].axis('off')

axes[1,0].hist(I.ravel(), bins=256, range=[0,256])

plt.show()

'''
● What does I.ravel() do in the above? Why has it been used?
The hist() function in Matplotlib expects a 1D array of values.
Since I is a 2D grayscale image (e.g., shape (height, width)), calling I.ravel() converts it to a 1D array.
This allows plt.hist() to analyze the pixel intensity distribution effectively.
'''
# ---------------------------- Task a ------------------------------
def implement_ab(image, percent = 2):

    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    max_index = np.where(hist == np.max(hist))[0][0]
    print(max_index)
    print(np.max(hist))

    for i in range(max_index):
        if hist[max_index-i] <= ((np.max(hist) * percent) / 100):
            a = max_index-i
            print('a =', a)
            break
    for i in range(max_index):
        if hist[max_index+i] <= ((np.max(hist) * percent) / 100):
            b = max_index + i
            print('b =', b)
            break
    return a, b


# b = 240
# a = 135
a, b = implement_ab(I)

J = (I-a) * 255.0 / (b-a)
J[J < 0] = 0
J[J > 255] = 255
J = J.astype(np.uint8)



f, axes = plt.subplots(2, 3)
# ---------------------------- Visualize Image J and it's Histogram ------------------------------

axes[0,1].imshow(J, 'gray', vmin=0, vmax=255)
axes[0,1].axis('off')

axes[1,1].hist(J.ravel(), bins=256, range=[0,256])




'''
● What does the above piece of code do?
Maps pixel values from the range [a, b] to [0, 255].

'''

# ---------------------------- Task b ------------------------------
K = cv2.equalizeHist(I)

axes[0, 2].imshow(K, 'gray', vmin=0, vmax=255)
axes[0, 2].axis('off')

axes[1, 2].hist(K.ravel(), bins=256, range=[0, 256])




plt.show()

'''
Compare the linearly histogram-expanded image with the histogram
equalization.



'''