import numpy as np
import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture('C:\\Users\\mandegar\\Documents\\courses\\Computer Vision\\LAB3\\cv-lab3\\egg.avi')

# Get video properties
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Width of the frame
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # Height of the frame
fps = int(cap.get(cv2.CAP_PROP_FPS))        # Frames per second

# Choose codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Create VideoWriter object
out = cv2.VideoWriter('C:\\Users\\mandegar\\Documents\\courses\\Computer Vision\\LAB3\\cv-lab3\\eggs-reverse.avi', fourcc, fps, (w, h))

frames = []  # List to store frames

# Read all frames and store them in a list
while True:
    ret, frame = cap.read()
    if not ret:  # End of video (or error)
        break
    frames.append(frame)

cap.release()  # Release video capture
# Write frames in reverse order
for frame in reversed(frames):
    out.write(frame)

out.release()  # Release output video

print("Reversed video saved successfully!")


'''
1. What happens if you press "q" before the video finishes?
If you press the "q" key, the condition if key == ord('q'): will be met, breaking the while loop. This causes the program to stop playing the video, release the video frames (cap.release()), and close all OpenCV windows (cv2.destroyAllWindows()).

2. What happens if you increase or decrease the cv2.waitKey(33) value?
If you increase the value (e.g., cv2.waitKey(300)), the delay between frames increases, making the video play slower.
If you decrease the value (e.g., cv2.waitKey(3)), the delay between frames decreases, making the video play faster.
The default value of 33 ms corresponds to a playback speed of around 30 frames per second (fps).

3. What happens if you replace cv2.waitKey(33) with cv2.waitKey(0) or cv2.waitKey()?
cv2.waitKey(0): The program pauses indefinitely at the first frame until a key is pressed. The video will not proceed automatically.
cv2.waitKey() (without an argument): It behaves similarly to cv2.waitKey(0), requiring a keypress to move forward.

'''