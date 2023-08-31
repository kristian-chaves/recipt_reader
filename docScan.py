from perspective_transform import four_point_transform
from skimage.filters import threshold_local
#from tkinter.filedialog import askopenfilename
import easygui

import numpy as np
#import argparse
import cv2
import imutils

img = easygui.fileopenbox()
#filename = askopenfilename()

print("hello world")

#load image, generate ratio of old:new heights, resize og image
    # resize makes detection faster + more accurate
image = cv2.imread(img)
ratio = image.shape[0] / 500.0
orig = image.copy
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

