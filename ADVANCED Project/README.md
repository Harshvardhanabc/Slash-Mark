# Slash-Mark-final-project

1. Import the necessary libraries:

   "cv2" : OpenCV library for computer vision tasks.

   "easyocr" : EasyOCR library for performing OCR.

2. Initialize the EasyOCR reader:

   reader = easyocr.Reader(['en'])

   This initializes an EasyOCR reader object for English text recognition.

3. Define a function perform_ocr(frame):

    This function takes a frame (image) as input and performs OCR on it.
  
    It converts the frame to RGB format (required by EasyOCR).
  
    It performs OCR using EasyOCR and extracts recognized text from the result.
  
    Finally, it returns the recognized text.

4. Define a function display_text(frame, text):

    This function takes a frame and recognized text as input.
  
    It displays the recognized text on the frame using OpenCV's cv2.putText()         function.

5. Define the main() function:

    This is the main entry point of the script.
  
    It initializes a video capture object (cap) to capture frames from the webcam.
  
    It continuously reads frames from the webcam and performs OCR on each frame.
  
    Recognized text is displayed on the frame using display_text() function.
  
    The frame with displayed text is shown in a window named "OCR".
  
    The loop exits if the 'q' key is pressed.
  
    Finally, it releases the video capture object and closes all OpenCV windows.

6. Execute the main() function if the script is run as the main program:

     if __name__ == "__main__":
         main()

     You can use this script to run live OCR on text captured by your webcam. Make sure you have OpenCV and EasyOCR installed in your Python environment.
