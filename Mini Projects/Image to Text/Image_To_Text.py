import pytesseract 
from PIL import Image 
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Dell\AppData\Local\Tesseract-OCR\tesseract.exe"
img = Image.open("Imagetotext.png") # Photo which to converted into text 
text = pytesseract.image_to_string(img)
print(f"Text Scanned: \n\n{text}")
