# Import required libraries
import pyautogui
import pytesseract
from PIL import Image
import smtplib
from email.mime.text import MIMEText

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to take a screenshot
def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot_path = "screenshot.png"
    screenshot.save(screenshot_path)
    return screenshot_path

# Function to extract text from image using OCR
def image_to_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

# Function to send email
def send_email(text):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "jayjchiringz@gmail.com"
    smtp_password = "krfy rfti ymna rliz"  # Replace with your app-specific password
    from_addr = "jayjchiringz@gmail.com"
    to_addr = "technothrone2014@gmail.com"

    msg = MIMEText(text)
    msg['Subject'] = 'Subject of your email'
    msg['From'] = from_addr
    msg['To'] = to_addr

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")

    finally:
        server.quit()

# Example usage:
if __name__ == "__main__":
    # Take a screenshot
    screenshot_path = take_screenshot()

    # Convert image to text
    extracted_text = image_to_text(screenshot_path)
    print("Extracted Text:")
    print(extracted_text)

    # Send the extracted text via email
    send_email(extracted_text)