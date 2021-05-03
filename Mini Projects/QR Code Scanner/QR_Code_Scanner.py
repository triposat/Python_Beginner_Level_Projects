from pyzbar.pyzbar import decode  # pip install pyzbar
from PIL import Image  # pip install PIL
# Jump the Image you want to Scan
a = decode(Image.open("C:\\Users\\Dell\\Downloads\\Try.png"))
print(f" Text Scanned :  {a[0][0]}")
