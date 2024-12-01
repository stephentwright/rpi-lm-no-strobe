import cv2
import numpy as np

def detect_golf_ball(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load image.")
        return

    # Resize the image for better processing (optional)
    resized_image = cv2.resize(image, (1440, 480))
    original_image = resized_image.copy()

    # Convert the image to grayscale
    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection
    edges = cv2.Canny(blurred, 25, 50)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    detected = False

    # Draw all contours on the original image
    cv2.drawContours(original_image, contours, -1, (255, 0, 0), 2)  # Blue contours with thickness 2

    for contour in contours:
        # Approximate the contour to a circle and calculate its properties
        ((x, y), radius) = cv2.minEnclosingCircle(contour)
        area = cv2.contourArea(contour)

        # Define criteria to identify a golf ball based on size and roundness
        if radius > 1   and radius < 50 and area / (np.pi * radius**2) > 0.8:
            # Mark the golf ball on the original image
            cv2.circle(original_image, (int(x), int(y)), int(radius), (255, 255, 255), 1)
            detected = True

    # Display the result
    cv2.imshow("Detected Golf Ball", original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if detected:
        print("Golf ball detected!")
    else:
        print("No golf ball detected.")

# Path to the input image
image_path = "0345.bmp"  # Replace with the path to your image
detect_golf_ball(image_path)
