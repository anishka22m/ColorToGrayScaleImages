import cv2
import os

# Path to the folder containing Spider Man images
folder_path = r"images\Spider_Man"

# List of supported image file extensions
supported_extensions = [".jpeg", ".jpg", ".png"]
count = 0
# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if any(filename.lower().endswith(ext) for ext in supported_extensions):
        # Construct the full path to the image
        img_path = os.path.join(folder_path, filename)
        
        # Read the image
        img = cv2.imread(img_path)
        
        # Convert to grayscale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Display image dimensions and show the grayscale image
        print(f"Image shape: {img_gray.shape}")
        cv2.imshow("Grayscale Image", img_gray)
        count+=1 
        print("Count: ",count)


        
        # Wait for a key press to move to the next image
        cv2.waitKey(0)

# Close all OpenCV window