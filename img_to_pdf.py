#! /usr/bin/python3
# Script developed by Luca Mannella, Politecnico di Torino, Turin, Italy

import sys
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PIL import Image

def convert_image_to_pdf(input_image_path, output_pdf_path):
    c = canvas.Canvas(output_pdf_path, pagesize=A4)
    
    # Get the dimensions of the A4 page
    page_width, page_height = A4
    
    # Get image size    
    image = Image.open(input_image_path)
    image_width, image_height = image.size
    
    # Calculate the position to center the image on the page
    x_offset = (page_width - image_width) / 2
    y_offset = (page_height - image_height) / 2
    
    c.drawImage(input_image_path, x_offset, y_offset, width=image_width, height=image_height)
    c.save()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python img_to_pdf.py input_image.png output.pdf")
        sys.exit(130)
    else:
        input_image_path = sys.argv[1]
        output_pdf_path = sys.argv[2]
        print(f'Converting image "{input_image_path}" into pdf "{output_pdf_path}"')
        convert_image_to_pdf(input_image_path, output_pdf_path)
        print(f'Converted. New pdf saved into: {output_pdf_path}')
