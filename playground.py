from PIL import Image
from pytesseract import pytesseract
import easygui


path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img_o = easygui.fileopenbox()


pytesseract.tesseract_cmd = path_to_tesseract

img = Image.open(img_o)

text = pytesseract.image_to_string(img)
print(text)



