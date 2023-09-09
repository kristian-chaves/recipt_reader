from PIL import Image
from pytesseract import pytesseract
import easygui


def image_to_string_auto(filename, path):
    filename = filename + path
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pytesseract.tesseract_cmd = path_to_tesseract
    img = Image.open(img_o)

