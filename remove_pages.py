#! /usr/bin/python3
# Script developed by Luca Mannella, Politecnico di Torino, Turin, Italy

import sys
from PyPDF2 import PdfReader, PdfWriter

def remove_pages(pdf_file, num_pages, direction, output_file):
    reader = PdfReader(pdf_file)
    writer = PdfWriter()

    if num_pages >= len(reader.pages):
        print("Error: The number of pages to remove is greater than or equal to the total number of pages in the PDF.")
        return

    if direction.lower() == 'top':
        start_page = num_pages
        end_page = len(reader.pages)
    elif direction.lower() == 'bottom':
        start_page = 0
        end_page = len(reader.pages) - num_pages
    else:
        print("Invalid direction. Please enter either 'top' or 'bottom'.")
        return

    for page_num in range(start_page, end_page):
        page = reader.pages[page_num]
        writer.add_page(page)

    with open(output_file, 'wb') as output_pdf:
        writer.write(output_pdf)


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Error: Missing arguments!")
        print("python remove_pages.py <input_file> <num_pages> <direction> [<output_file>]")
        sys.exit(130)
    if len(sys.argv) > 4:
        print("Error: Too many argument!")
        print("python remove_pages.py <input_file> <num_pages> <direction> [<output_file>]")
        sys.exit(131)
        
    pdf_file = sys.argv[1]
    num_pages = int(sys.argv[2])
    direction = sys.argv[3]
    if len(sys.argv) == 4:
        output_file = sys.argv[3]
    else:
        output_file = 'new_' + pdf_file
    
    remove_pages(pdf_file, num_pages, direction, output_file)
