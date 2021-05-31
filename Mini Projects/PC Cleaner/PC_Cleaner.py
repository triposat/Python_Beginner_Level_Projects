import os
# Jump to the folder where you to create a new folder for your files
os.chdir("C:\\Users\\Dell\\Desktop\\All C Programs")


def create(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)


def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")


files = os.listdir()
create("Only C Programs")  # Create Folder for your files
C = ['.c']  # The folder only consist of files with extension .c
Cs = [file for file in files if os.path.splitext(file)[1].lower() in C]
# Move files to the new folder, only .c files will be moved
move("Only C Programs", Cs)
