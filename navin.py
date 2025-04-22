from pytesseract import pytesseract
import os

class OCR:
    def __init__(self):
       self.path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    def extract(self,filename):
        try:
            pytesseract.tesseract_cmd = self.path

            text = pytesseract.image_to_string(filename)
            return text
        except Exception as e:
            print(e)
            return "ERROR"

ocr = OCR()
text = ocr.extract("12.png")
print(text)