import numpy as np
import cv2

# Load the image in grayscale and normalize to [0,1]
I = cv2.imread(r"C:\Users\mandegar\Documents\courses\Computer Vision\LAB4\cameraman.png", cv2.IMREAD_GRAYSCALE)
I = I.astype(np.float32) / 255.0  # Ensure pixel values are in [0,1]

noise_sigma = 0.05  # initial noise standard deviation

while True:
    # TODO: Create a noise image N using a Gaussian distribution with mean 0 and variance noise_sigma^2.
    # Hint: Use np.random.randn with the shape of I and multiply by noise_sigma.
     N = np.random.randn(*I.shape) * noise_sigma
     J = np.clip(I + N, 0.0, 1.0)
     cv2.imshow('Snow Noise', J)

     key = cv2.waitKey(33) & 0xFF

    # TODO: Adjust noise_sigma based on key input:
     if key == ord('u'):
        noise_sigma = min(noise_sigma + 0.01, 1.0)  # Cap at 1.0
     elif key == ord('d'):
        noise_sigma = max(noise_sigma - 0.01, 0.01)  # Minimum 0.01
     elif key == ord('q'):
         break

cv2.destroyAllWindows()

'''
● What does normalizing the image to [0,1] (the line with
I.astype(np.float32)/255.0) accomplish in terms of noise addition?
If we say "add noise with strength σ = 0.1", it means the noise will change pixel values by about ±0.1 (10% of the brightness range).
If we didn’t normalize, σ = 0.1 would be tiny (since pixels go up to 255), and the noise would be almost invisible.


● Why should the noise image be regenerated inside the loop instead of outside? What
happens if you create N once before the loop and reuse it every frame?
Regenerating N in each loop iteration creates fresh random noise every frame, simulating realistic noise (like a live camera feed).

● Ensure your code never uses a negative noise_sigma. Why is a negative standard
deviation meaningless for noise generation?
Standard deviation (σ) is defined as the square root of variance (σ²), which is always non-negative.


'''