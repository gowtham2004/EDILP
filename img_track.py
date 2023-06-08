import cv2
import numpy as np

def track_image(image, window_name):
    """
    Track an image and show its current position in a window.

    Args:
        image: The image to track.
        window_name: The name of the window to display the image in.
    """

    # Create a window to display the image.
    cv2.namedWindow(window_name)

    # Load the image into memory.
    image_np = np.array(image)

    # Create a tracker object.
    tracker = cv2.TrackerKCF_create()

    # Start tracking the image.
    tracker.init(image_np, (0, 0, image_np.shape[1], image_np.shape[0]))

    # Display the current position of the image on the window.
    while True:
        # Get the current position of the image.
        pos = tracker.update(image_np)

        # Display the position of the image on the window.
        cv2.rectangle(image_np, pos, (pos[0] + image_np.shape[1], pos[1] + image_np.shape[0]), (255, 0, 0), 2)

        # Display the image on the window.
        cv2.imshow(window_name, image_np)

        # Check if the user wants to quit.
        key = cv2.waitKey(1)
        if key == 27:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Load the image to track.
    image = cv2.imread("image.jpg")

    # Track the image and show its current position in a window.
    track_image(image, "Image Tracker")
