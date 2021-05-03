import os
# Jump to directory where you want to edit extension
os.chdir("C:\\Users\\Dell\\Desktop\ha")
files = os.listdir()
C = ['.pdf']
Cs = [file for file in files if os.path.splitext(file)[1].lower() in C]
for i in Cs:
    base = os.path.splitext(i)[0]
    os.rename(i, base + '.docx')
