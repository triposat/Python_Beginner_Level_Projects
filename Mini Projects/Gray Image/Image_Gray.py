import cv2
img = cv2.imread("one.jpg")  # Image that you want to grey...
clahe = cv2.createCLAHE()
grey_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
enhc_img = clahe.apply(grey_img)
# It will save the Image as "one_one" after greying it...
cv2.imwrite("one_one.jpg", enhc_img)
