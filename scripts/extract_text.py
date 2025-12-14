# pip3 install paddleocr paddlepaddle
# pip3 install --upgrade pip

# PaddleOCR Does Not Support PDFs Directly So They Must Be Converted To Images First

# pip install pdf2image pillow
# brew install poppler

from paddleocr import PaddleOCR, draw_ocr # Main OCR Dependencies
from pdf2image import convert_from_path # PDF To Image Conversion
from matplotlib import pyplot as plt # Plot Images
import cv2 # OpenCV
import os # Folder Directory Navigation System  

# Initialize Model 
ocr_model = PaddleOCR(use_angle_cls=True, lang='en') # use_angle_cls enables angle classifier to automatically detect and correct text that is roatated by 90, 180, 270 degrees

# Path To The Uploaded PDF File
pdf_path = 'RAG-Notes/data/raw/CIS*2030 Week 11 Notes.pdf'
# Path To Where The Outputed Image Will Be Saved 
output_dir = 'RAG-Notes/data/processed/'

# Make Output Directory If It Does Not Already Exist
os.makedirs(output_dir, exist_ok=True)

# Convert PDF To Images
pages = convert_from_path(pdf_path, dpi=300)

all_text = []

# Iterate Through Each Page
for i, page in enumerate(pages):

    # Path To Save The Image In The Output Directory With The Page Number
    img_path = f"{output_dir}page_{i+1}.png"
    # Save The Image
    page.save(img_path, 'PNG')

    #********************************************************
    # pdf_path -> Uploaded PDF File(s)                      *
    # output_dir -> Directory The Images Will Be Saved To   * 
    # img_path -> Path To The Current Image Being Processed *
    #********************************************************

    # Run The OCR Method On The OCR Model
    result = ocr_model.ocr(img_path, cls=True)

    # Extract Text From The Result

