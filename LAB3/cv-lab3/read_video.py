import numpy as np
import cv2

# create a VideoCapture object
cap = cv2.VideoCapture('C:\\Users\\mandegar\\Documents\\courses\\Computer Vision\\LAB3\\cv-lab3\\kntu-computer.avi')

# sometimes this is needed:
#if not cap.isOpened():
#    cap.open();


while True:
    
    # Capture frame-by-frame
    ret, I = cap.read()
    
    if ret == False: # end of video (perhaps)
        break

    # Display I
    cv2.imshow('win1',I)
    
    key = cv2.waitKey() # ~ 30 frames per second

    if key & 0xFF == ord('q'): 
        break


cap.release()
cv2.destroyAllWindows()

'''
What happens by pressing "q" before the video finishes? (replace "key ==
ord('q')" by "key & 0xFF == ord('q')" if the above fails.

When you press the "q" key before the video finishes, the program detects the key press event inside the while loop and breaks out of the loop. 
replacement is because cv2.waitKey() returns an integer, but on some systems (especially on macOS or some Windows setups), only the last byte
 of the key press is needed to compare it with ASCII values. The & 0xFF operation ensures that only the least significant byte is compared, 
 preventing issues related to how OpenCV handles key input on different platforms.

 What happens?

The video will pause at the first frame and will not continue playing until a key is pressed.
cv2.waitKey(0) makes the program wait indefinitely for a key press before moving to the next frame.
This means you will have to press a key for every single frame of the video, making it impractical for video playback.

cv2.waitKey(0) or cv2.waitKey(): The video pauses at the first frame, requiring manual key presses to proceed frame by frame.


'''
