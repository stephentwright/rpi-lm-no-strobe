import cv2
import numpy as np

def detect_ball_and_crop(image_path):
    
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
        # Get the first detected circle
        circles = np.uint16(np.around(detected_circles))
        for idx, (x, y, r) in enumerate(circles[0, :]):
            # Define square coordinates around the circle
            top_left_x = max(0, x - r - 20)
            top_left_y = max(0, y - r - 20)
            bottom_right_x = min(image.shape[1], x + r + 20)
            bottom_right_y = min(image.shape[0], y + r + 20)
            
            # add the detected circle around the crop
            cv2.circle(gray, (x, y), r, (0, 255, 0), 1)      
            
            # Crop the square region
            cropped_image = gray[top_left_y:bottom_right_y, top_left_x:bottom_right_x]
                  
            # Save the cropped image
            cv2.imshow(f"circle_{idx + 1}", cropped_image)

            # Save the cropped image
            output_path = f"{image_path}-circle_{idx + 1}.jpg"
            cv2.imwrite(output_path, cropped_image)
            
        # Save the cropped image
        cv2.imshow("original image", image)
        cv2.waitKey(0)

    else:
        print("No circles were detected.")

    # Close all OpenCV windows
    cv2.destroyAllWindows()

# Example usage
image_path = "./media/0345.bmp"  # Replace with the path to your image
detect_ball_and_crop(image_path)
