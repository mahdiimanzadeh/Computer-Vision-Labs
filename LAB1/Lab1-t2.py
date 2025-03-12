img_path = 'masoole-gray.png'
import PIL.Image as Image

image = Image.open(img_path)
image
import numpy as np

# Convert the image to a NumPy array
img_array = np.array(image)  # 'image' should be your image object loaded with Pillow

# Flip the image vertically (upside down)
shif = np.flipud(img_array)  # flipud reverses the array along the vertical axis

# Concatenate the original and flipped images vertically (stacked on top of each other)
concatenated_img_array = np.vstack((img_array, shif))  # vstack stacks arrays along the vertical axis

# Convert the concatenated NumPy array back into a Pillow image
concatenated_img = Image.fromarray(concatenated_img_array)  # Convert NumPy array back to image

# Show the concatenated image
concatenated_img  # Display the final image