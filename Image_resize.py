import cv2
import os

def resize_images_in_folder(input_folder, output_folder, target_width, target_height, quality=70):
    """
    Resizes all images in a folder and saves them to a new folder.

    Args:
        input_folder (str): Path to the folder containing the input images.
        output_folder (str): Path to the folder to save the resized images.
        target_width (int): Desired width of the resized images.
        target_height (int): Desired height of the resized images.
        quality (int): JPEG compression quality (0-100, higher is better).
    """

    if not os.path.exists(output_folder):
        os.makedirs(output_folder) # Create output folder if it doesn't exist

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.tif')): #Check for image file extensions
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                img = cv2.imread(input_path)

                if img is None:
                    print(f"Error: Could not read image {filename}")
                    continue # Skip to the next file

                resized_img = cv2.resize(img, (target_width, target_height), interpolation=cv2.INTER_AREA)

                if filename.lower().endswith(('.png')):
                  cv2.imwrite(output_path, resized_img, [cv2.IMWRITE_PNG_COMPRESSION, 3]) #png compression
                else:
                  cv2.imwrite(output_path, resized_img, [cv2.IMWRITE_JPEG_QUALITY, quality]) #jpg compression
                print(f"Resized {filename} and saved to {output_path}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage:
input_folder_path = "C:/Users/samsi/Desktop/Yolov8/Pictures-from-Video"  # Replace with your input folder path
output_folder_path = "C:/Users/samsi/Desktop/Yolov8/Resized-Pictures" # Replace with your output folder path
new_width = 544
new_height = 960
compression_quality = 70

resize_images_in_folder(input_folder_path, output_folder_path, new_width, new_height, compression_quality)