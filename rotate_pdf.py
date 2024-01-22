#! /usr/bin/python3
# Script developed by Luca Mannella, Politecnico di Torino, Turin, Italy

import sys
import PyPDF2

def rotate_pdf(input_path, output_path):
    """Rotate every pdf page by 90 degrees right."""
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(len(pdf_reader.pages)):           
            page = pdf_reader.pages[page_num]
            page.rotate(90)  # Rotate 90 degrees right
            pdf_writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Error: Missing arguments!")
        print("rotate_pdf.py <input> [<output>]")
        sys.exit(130)
    
    if len(sys.argv) > 3:
        print("Error: Too many argument!")
        print("rotate_pdf.py <input> [<output>]")
        sys.exit(131)
        
    output_pdf_path = input_pdf_path = sys.argv[1]
    if len(sys.argv) == 3:
        output_pdf_path = sys.argv[2]

    rotate_pdf(input_pdf_path, output_pdf_path)

    print(f"Rotated. New PDF saved into: {output_pdf_path}")
