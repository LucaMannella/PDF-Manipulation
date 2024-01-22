#! /usr/bin/python3
# Script developed by Luca Mannella, Politecnico di Torino, Turin, Italy

import PyPDF2
import sys

def split_pdf(input_pdf, page_number):
    """Split the pdf into two different pdf files."""
    try:
        with open(input_pdf, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            pdf1 = PyPDF2.PdfWriter()
            pdf2 = PyPDF2.PdfWriter()
            
            # Split the input PDF into two parts
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                if page_num + 1 <= page_number:
                    pdf1.add_page(page)
                else:
                    pdf2.add_page(page)
            
            # Save the two split PDFs
            with open('part1.pdf', 'wb') as output_file1:
                pdf1.write(output_file1)
            
            with open('part2.pdf', 'wb') as output_file2:
                pdf2.write(output_file2)
            
        print(f"PDF '{input_pdf}' split successfully into 'part1.pdf' and 'part2.pdf'")
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    if len(sys.argv) <= 2 or len(sys.argv) > 3:
        print("Usage: python split_pdf.py <input.pdf> <page_number>")
        sys.exit(1)

    split_pdf(sys.argv[1], int(sys.argv[2]))
