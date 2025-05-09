import cv2
import os

# Path to the input AVI video file
input_video_path = 'C:/Users/samsi/Desktop/Yolov8/Main-Video/VK.mp4'




# Directory where you want to save the images
output_image_dir = 'C:/Users/samsi/Desktop/Yolov8/Pictures-from-Video'

# Create the output image directory if it doesn't exist
os.makedirs(output_image_dir, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(input_video_path)

# Initialize frame count
frame_count = 0

# Initialize a timer for capturing frames at the start of each second
second_timer = 0

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Break the loop if we have reached the end of the video
    if not ret:
        break

    # Check if it's time to capture a frame at the start of a second
    if frame_count >= int(cap.get(cv2.CAP_PROP_FPS) * second_timer):
        # Save the frame as an image
        image_filename = os.path.join(output_image_dir, f'frame_{frame_count:04d}.jpg')
        cv2.imwrite(image_filename, frame)

        # Increment the second timer to capture the next frame in the next second
        second_timer += 1

    # Increment frame count
    frame_count += 1

# Release the video capture object
cap.release()

# Print the total number of frames saved
print(f'Total frames saved as images: {frame_count}')
