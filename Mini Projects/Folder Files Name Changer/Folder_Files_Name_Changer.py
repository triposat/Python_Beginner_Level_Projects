import os


def soldier(path, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    for s in files:
        os.rename(s, s.upper())
        if os.path.splitext(s)[1] == format:
            os.rename(s, f"Put here name{i}{format}")
            i += 1


soldier(r"C:\Users\Dell\Desktop\C trial", ".JPG")
# It will jump to This path given above and search for "JPG" file and then change the name...
