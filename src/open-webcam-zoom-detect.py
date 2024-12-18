import cv2
import numpy as np

def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Set the frame dimensions (optional, depending on your webcam's capabilities)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Unable to capture video.")
            break

        # Define the region of interest (ROI) - center of the frame
        height, width, _ = frame.shape
        roi_size = 200  # Size of the zoomed region
        center_x, center_y = width // 2, height // 2
        x1 = max(center_x - roi_size // 2, 0)
        y1 = max(center_y - roi_size // 2, 0)
        x2 = min(center_x + roi_size // 2, width)
        y2 = min(center_y + roi_size // 2, height)

        # Crop the ROI
        roi = frame[y1:y2, x1:x2]

        # Zoom into the ROI by resizing it to the original frame size
        zoomed_frame = cv2.resize(roi, (width, height))

        # Convert to grayscale for Hough Circle detection
        gray = cv2.cvtColor(zoomed_frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)

        # Detect circles using HoughCircles
        circles = cv2.HoughCircles(
            gray_blurred, 
            cv2.HOUGH_GRADIENT, 
            dp=1.2, 
            minDist=50, 
            param1=100, 
            param2=30, 
            minRadius=10, 
            maxRadius=100
        )

        # If circles are detected, draw them on the frame
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for circle in circles[0, :]:
                x, y, r = circle
                cv2.circle(zoomed_frame, (x, y), r, (0, 255, 0), 2)  # Draw circle
                cv2.circle(zoomed_frame, (x, y), 2, (0, 0, 255), 3)  # Draw center
                cv2.putText(zoomed_frame, "Ball Detected", (x - 20, y - r - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Display the zoomed frame
        cv2.imshow('Zoomed Frame', zoomed_frame)
        cv2.imshow('WC Frame', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
