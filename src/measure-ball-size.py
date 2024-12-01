import cv2
import numpy as np

# Global variables to store user selection
selected_circle = None
circles = None
image = None

def mouse_event(event, x, y, flags, param):
    global selected_circle, circles, image

    if event == cv2.EVENT_LBUTTONDOWN:
        # Check which circle the user clicked
        for idx, (cx, cy, r) in enumerate(circles):
            if (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2:
                selected_circle = (cx, cy, r)
                print(f"Circle {idx + 1} selected: Center=({cx}, {cy}), Radius={r} pixels")
                # Highlight the selected circle
                output_image = image.copy()
                cv2.circle(output_image, (cx, cy), r, (0, 255, 0), 4)
                cv2.rectangle(output_image, (cx - 5, cy - 5), (cx + 5, cy + 5), (0, 128, 255), -1)
                cv2.imshow("Ball Detection", output_image)
                break

def detect_ball_and_measure_radius(image_path):
    global selected_circle, circles, image

    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load the image.")
        return

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)

    # Detect circles using Hough Circle Transform
    detected_circles = cv2.HoughCircles(
        blurred,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=500,
        param1=50,
        param2=30,
        minRadius=10,
        maxRadius=50
    )

    if detected_circles is not None:
        circles = np.round(detected_circles[0, :]).astype("int")

        # Draw all detected circles
        temp_image = image.copy()
        for idx, (x, y, r) in enumerate(circles):
            cv2.circle(temp_image, (x, y), r, (0, 255, 0), 2)
            cv2.putText(temp_image, f"{idx + 1}", (x - 20, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

        # Show the image and set up mouse callback
        cv2.imshow("Ball Detection", temp_image)
        cv2.setMouseCallback("Ball Detection", mouse_event)

        # Wait until the user selects a circle
        print("Click on the correct circle to select it.")
        cv2.waitKey(0)

        if selected_circle:
            cx, cy, r = selected_circle
            print(f"Final Selection: Center=({cx}, {cy}), Radius={r} pixels")
        else:
            print("No circle selected.")
    else:
        print("No circles detected.")

    # Close all OpenCV windows
    cv2.destroyAllWindows()

# Example usage
image_path = "0344.bmp"  # Replace with the path to your image
detect_ball_and_measure_radius(image_path)
