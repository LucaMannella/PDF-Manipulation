#! /usr/bin/python3
# Script developed by Luca Mannella, Politecnico di Torino, Turin, Italy

import sys
import PyPDF2
from collections import Counter

def count_words_in_pdf(file_path):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        # Create a PDF file reader object
        reader = PyPDF2.PdfReader(file)
        
        # Initialize a counter for words
        words = Counter()
        
        # Loop through each page in the PDF
        for page_num in range(len(reader.pages)):
            # Extract the text from the page
            text = reader.pages[page_num].extract_text()
            
            # Split the text into words and update the counter
            words.update(text.split())
        
    # Return the counter
    return words


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Error: Missing arguments!")
        print("python pdf_word_counter.py <file1> [files]")
        sys.exit(130)
        
    total_words = 0
    
    for i in range(1, len(sys.argv)):
        file = (sys.argv[i])
        word_counts = count_words_in_pdf(file)
        words = sum(word_counts.values())
        print(f'Total words of {file}: {words}')
        total_words += words
    
    print(f'Total words: {total_words}')
