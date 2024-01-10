# from PIL import Image as pil_image
# from pytesseract import pytesseract
# pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# img = pil_image.open("E:\\Documents\\asmi\\main\\media\\img\\test.png")
# text = pytesseract.image_to_string(img)
# print(text)

from PyPDF2 import PdfReader 
import os
# creating a pdf reader object 
current_directory = os.getcwd()
print(current_directory)
reader = PdfReader(current_directory+'/media/pdf/sample.pdf'.replace("/","\\"))
print(len(reader.pages)) 
  
page = reader.pages[0]
  
# extracting text from page 
text = page.extract_text() 
print(text)
