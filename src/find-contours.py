import cv2
import numpy as np

# Load and preprocess the image
image = cv2.imread('./media/0345.bmp-circle_2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 25, 150, apertureSize=3, L2gradient=False)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

for contour in contours:
    area = cv2.contourArea(contour)
    print(area)
    if 0 < area < 5000:  # Filter based on expected size
        (x, y), radius = cv2.minEnclosingCircle(contour)
        circularity = (4 * np.pi * area) / (cv2.arcLength(contour, True) ** 2)
        cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 0), 2)
        
        if 0.85 <= circularity <= 1.15:  # Ensure it's circular
            # Draw the ball
            cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 0), 2)
            print(f"Ball found at ({x}, {y}) with radius {radius}")

cv2.imshow('Detected Ball', image)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
