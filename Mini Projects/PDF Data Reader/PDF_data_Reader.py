import PyPDF2
import os
# Jump to location where PDF file is present
os.chdir(r"C:\Users\Dell\Desktop")
pdfobj = open("Try.pdf", "rb")
pdfread = PyPDF2.PdfFileReader(pdfobj)
page = pdfread.getPage(0)  # Want to read only first page
print(page.extractText())  # Extracting text from the PDF and print it.
