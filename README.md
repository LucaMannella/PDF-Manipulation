# PDF-Manipulation

A set of Python script to manipulate PDF files.

## img_to_pdf.py

Convert an image into a pdf. The image is put in the center of a A4 page.

Usage:
```bash
	python img_to_pdf.py input_image.png output.pdf
```

## pdf_word_counter.py

Count the number of words in one or more PDF file.
If many files are specified, the script prints the number of word for each file and the overall number of words.

Usage:
```bash
	python pdf_word_counter.py <file1> [files]
```

## remove_pages.py

Remove a specified number of page from the beginning or the end of a pdf file given as parameter.

The name of the output file is optional. Direction can be: "top" or "bottom".

```bash
python remove_pages.py <input_file> <num_pages> <direction> [<output_file>]
```

## rotate_pdf.py

Rotate every page inside a PDF by 90 degrees right.

The name of the output file is optional.

```bash
python remove_pages.py <input_file> <num_pages> <direction> [<output_file>]
```

## split_pdf.py

Split a pdf file into two different pdfs. The first pdf will be composed by a number of page equal to `page_number`. The second pdf by all the others.

```bash
python split_pdf.py <input.pdf> <page_number>
```
