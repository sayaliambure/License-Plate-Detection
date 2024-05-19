# Import necessary libraries
import cv2
import pytesseract

# Function to read and extract text from an image
def extract_text_from_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding (optional, improves OCR accuracy in some cases)
    _, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Use pytesseract to extract text
    text = pytesseract.image_to_string(binary_image)

    return text

# Path to the image file
image_path = 'yolov8/data/images/training/img1.jpg'

# Extract text from the image
extracted_text = extract_text_from_image(image_path)
print(extracted_text)