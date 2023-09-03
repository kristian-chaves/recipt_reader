from perspective_transform import four_point_transform
from skimage.filters import threshold_local
#from tkinter.filedialog import askopenfilename
import easygui

import numpy as np
#import argparse
import cv2
import imutils
from datetime import datetime
import os

img = easygui.fileopenbox()
#filename = askopenfilename()

print("hello world")

#load image, generate ratio of old:new heights, resize og image
    # resize makes detection faster + more accurate
image = cv2.imread(img)
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height=500)

#convert image grey scale, blur -> find edges
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5,5), 0)
edged = cv2.Canny(gray, 75, 200)

#show original image and edge detected image
print("step 1: edge detection")
cv2.imshow("image", image)
cv2.imshow("edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

#find contours in image, keep only largest, initalize screen contour
    # find long lines
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    #if contour has four points, screen found
    if len(approx) == 4:
        screenCnt = approx
        break

print("step 2: find contours of paper")
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
cv2.imshow("outline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

warped = four_point_transform(orig, screenCnt.reshape(4,2) * ratio)

#make image black and white
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset = 10, method = "gaussian")
warped = (warped > T).astype("uint8") * 255

print("step 3: apply perspective transform")
cv2.imshow("original", imutils.resize(orig, height = 650))
cv2.imshow("scanned", imutils.resize(warped, height = 650))
img = imutils.resize(warped, height = 650)
cv2.waitKey(0)

current_time = datetime.now()  
filename = current_time.strftime("%Y_%m_%d_%H_%M_%S.png")

path = str(os.getcwd())
path = path + "\images"
os.chdir(path)
cv2.imwrite(filename, img)

