import cv2
import easyocr

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Function to perform OCR on the entire frame using EasyOCR
def perform_ocr(frame):
    # Convert the frame to RGB (EasyOCR expects RGB format)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform OCR using EasyOCR
    result = reader.readtext(frame_rgb)

    # Extract recognized text
    text = ""
    for detection in result:
        text += detection[1] + "\n"

    return text.strip()

# Function to display recognized text on the frame
def display_text(frame, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    font_color = (255, 255, 255)
    line_type = 1

    # Display the recognized text on the frame
    cv2.putText(frame, text, (20, 40), font, font_scale, font_color, line_type)

# Main function
def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Perform OCR on the frame
        text = perform_ocr(frame)

        # Display the recognized text on the frame
        display_text(frame, text)

        # Display the frame
        cv2.imshow('OCR', frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
