import cv2

def capture_and_crop(image_path):

    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load the image.")
        return

    # print("Press 'Space' to capture an image or 'q' to quit.")
    # while True:
    #     ret, frame = cap.read()
    #     if not ret:
    #         print("Error: Failed to capture image.")
    #         break

    #     # Show the live video feed
    #     cv2.imshow("Webcam", frame)

    #     key = cv2.waitKey(1) & 0xFF
    #     if key == ord(' '):  # Press Space to capture
    #         break
    #     elif key == ord('q'):  # Press q to quit
    #         cap.release()
    #         cv2.destroyAllWindows()
    #         return

    # # Release the webcam and close live video feed
    # cap.release()
    # cv2.destroyAllWindows()

    # Clone the captured image
    # clone = frame.copy()
    clone = image.copy()

    crop_width, crop_height = 1440, 480
    overlay_position = [0, 0]  # Top-left corner of the overlay

    def draw_overlay(event, x, y, flags, param):
        """
        Draws a 200x100 rectangle overlay with a circle in the bottom-left corner.
        """
        nonlocal overlay_position, clone
        temp_image = clone.copy()
        if event == cv2.EVENT_MOUSEMOVE:
            # Update overlay position (ensure it stays within the image boundaries)
            # overlay_position = [
            #     min(x, frame.shape[1] - crop_width),
            #     min(y, frame.shape[0] - crop_height),
            # ]
            overlay_position = [
                min(x, image.shape[1] - crop_width),
                min(y, image.shape[0] - crop_height),
            ]
            top_left = (overlay_position[0], overlay_position[1])
            bottom_right = (overlay_position[0] + crop_width, overlay_position[1] + crop_height)
            bottom_left_circle = (overlay_position[0] + 120, overlay_position[1] + crop_height - 120)

            # Draw the crop box
            cv2.rectangle(temp_image, top_left, bottom_right, (0, 255, 0), 2)
            # Draw the circle in the bottom-left corner
            cv2.circle(temp_image, bottom_left_circle, 30, (255, 0, 0), -1)  # Filled blue circle
            cv2.imshow("Hitting area calibration", temp_image)

        elif event == cv2.EVENT_LBUTTONDOWN:
            # Perform the crop when user clicks
            x_start, y_start = overlay_position
            # cropped = frame[y_start:y_start + crop_height, x_start:x_start + crop_width]
            cropped = image[y_start:y_start + crop_height, x_start:x_start + crop_width]

            # Display the cropped region
            cv2.imshow("Cropped Image", cropped)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # Print the crop coordinates
            print(f"Crop coordinates: Top-left ({x_start}, {y_start}), "
                  f"Bottom-right ({x_start + crop_width}, {y_start + crop_height})")

    print("Move the mouse to position the crop box, then click to select.")
    
    cv2.imshow("Hitting area calibration", clone)
    cv2.setMouseCallback("Hitting area calibration", draw_overlay)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Run the program
image_path = 'camera-resolution.jpg'
capture_and_crop(image_path)
