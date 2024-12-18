import cv2
import numpy as np

# Load the image
image = cv2.imread('./media/0345.bmp-circle_2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Preprocess the image: Apply Gaussian Blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny Edge Detection
# The two thresholds control edge linking; adjust them based on your image
low_threshold = 20
high_threshold = 100
edges = cv2.Canny(blurred, low_threshold, high_threshold)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Edges Detected', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
