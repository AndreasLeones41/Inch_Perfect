import os
from pdf2image import convert_from_path
import pytesseract

def pdf_to_text(pdf_path, output_txt="c:\\Users\\ather\\OneDrive\\Documents\\KurdishOutput2025(3).txt"):
    # Convert PDF to images
    images = convert_from_path(pdf_path)

    extracted_text = ""

    for i, img in enumerate(images):
        # Perform OCR using Tesseract
        text = pytesseract.image_to_string(img, lang="ckbLayer+eng")  # Add other languages if needed
        extracted_text += text + "\n\n"

        print(f"Processed page {i+1}/{len(images)}")

    # Save extracted text to file
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(extracted_text)

    print(f"Text extracted and saved to {output_txt}")

# Add the file here
pdf_to_text("c:\\Users\\ather\\KurdishFile.pdf")
