import PyPDF2
import os
os.chdir(r"C:\Users\Dell\Desktop")
pdfobj = open("Try.pdf", "rb")  # PDG you want to rotate
pdfread = PyPDF2.PdfFileReader(pdfobj)
pdfwrite = PyPDF2.PdfFileWriter()
# rotation=180
rotation = 270
for page in range(pdfread.numPages):
    pageobj = pdfread.getPage(page)
    pageobj.rotateClockwise(rotation)
    pdfwrite.addPage(pageobj)

new = open('Rotate_python.pdf', 'wb')  # New Rotate PDF
pdfwrite.write(new)
pdfobj.close()
new.close()
