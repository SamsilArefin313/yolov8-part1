import imgaug.augmenters as iaa
import cv2
import glob
import numpy as np
import os

# 1. Load Dataset
images = []
images_path = glob.glob("C:/Users/samsi/Desktop/Yolov8/Resized-Pictures/*.jpg")
for img_path in images_path:
    img = cv2.imread(img_path)
    if img is not None:
        images.append(img)
    else:
        print(f"Failed to load image: {img_path}")

# 2. Image Augmentation
augmentation = iaa.Sequential([
    # 1. Flip
    iaa.Fliplr(0.5),
    iaa.Flipud(0.5),

    # 2. Affine
    iaa.Affine(translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
               rotate=(-30, 30),
              scale=(0.5, 1.5)),

    # 3. Multiply
    iaa.Multiply((0.8, 1.2)),

    # 4. Linearcontrast
    iaa.LinearContrast((0.6, 1.4)),

    # Perform methods below only sometimes
    iaa.Sometimes(0.5,
        # 5. GaussianBlur
        iaa.GaussianBlur((0.0, 3.0))
    )
])

# 3. Save Augmented Images
output_directory = "C:/Users/samsi/Desktop/Yolov8/Augmented-Pictures"
os.makedirs(output_directory, exist_ok=True)  # Create the output directory if it doesn't exist

for i in range(5):  # Augment and save images 10 times (you can adjust this number)
    augmented_images = augmentation(images=images)
    for j, img in enumerate(augmented_images):
        output_path = os.path.join(output_directory, f"augmented_{i}_{j}.jpg")
        cv2.imwrite(output_path, img)

print(f"Augmented images saved to: {output_directory}")
