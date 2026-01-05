# pip3 install paddleocr paddlepaddle
# pip3 install --upgrade pip

# PaddleOCR Does Not Support PDFs Directly So They Must Be Converted To Images First

# pip install pdf2image pillow
# brew install poppler

from paddleocr import PaddleOCR # Main OCR Dependencies
from pdf2image import convert_from_path, pdfinfo_from_path # PDF To Image Conversion
import os # Folder Directory Navigation System  
import gc # Garbage Collection To Free RAM

# Initialize Model 
ocr_model = PaddleOCR(use_textline_orientation=True, lang='en') # use_textline_orientation enables angle classifier to automatically detect and correct text that is roatated by 90, 180, 270 degrees

# Path To The Uploaded PDF File
pdf_path = 'data/raw/CIS2030_Week_11_Notes.pdf'
# Path To Where The Outputed Image Will Be Saved 
output_dir = 'data/processed'

# Make Output Directory If It Does Not Already Exist
os.makedirs(output_dir, exist_ok=True)

# Get The Total Number Of Pages In The PDF
info = pdfinfo_from_path(pdf_path)
total_pages = info['Pages']

all_text = []

# Iterate Through Each Page
for i in range(1, total_pages + 1):

    print(f"Processing Page {i} of {total_pages}")

    # Convert The Current Page To An Image
    page = convert_from_path(pdf_path, dpi=200, first_page=i, last_page=i)[0]

    # Path To Save The Image In The Output Directory With The Page Number
    img_path = f"{output_dir}/page_{i}.png"

    # Save The Image
    page.save(img_path, 'PNG')

    #********************************************************
    # pdf_path -> Uploaded PDF File(s)                      *
    # output_dir -> Directory The Images Will Be Saved To   * 
    # img_path -> Path To The Current Image Being Processed *
    #********************************************************

    # Run The OCR Method On The OCR Model
    result = ocr_model.predict(img_path)

    page_lines = []

    # If A Result Was Extracted From The Image
    if result:

        # Iterate Through Each Line In The Result
        for line in result:

            # Get The Extracted Text And Confidence Score
            text = line.get('text', '')
            confidence = line.get('score', 0)

            # Appends The Text From The Line If The Confidence Is Above 0.4 And Is Not Empty
            if confidence >= 0.4 and text.strip():
                page_lines.append(text)
        
    # Appends The Extracted Text To The All Text List
    all_text.append('\n'.join(page_lines))

    # Deleates The Image After Processing To Free Up RAM
    del page 
    gc.collect()

# Combines All The Extracted Text From Each Page Into A Single String
final_text = '\n\n'.join(all_text) 

print("\n--- EXTRACTED TEXT ---\n")

# Prints The Final Extracted Text
print(final_text)