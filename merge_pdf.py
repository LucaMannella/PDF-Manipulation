#! /usr/bin/python3
# Script developed by Luca Mannella, Politecnico di Torino, Turin, Italy

from pypdf import PdfMerger
import sys

def merge_pdf(output, inputs):
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(output)
    merger.close()

if __name__ == "__main__":
    if len(sys.argv) <= 3:
        print("Error: Missing arguments!")
        print("merge_pdf.py <output> <input1> [<...inputs...>] ")
        sys.exit(130)

    pdfs = sys.argv[2:len(sys.argv)]
    output = sys.argv[1]
    print(f"Inputs: {pdfs}")
    merge_pdf(output, pdfs)
    print(f"Merged. New pdf save into: {output}")
