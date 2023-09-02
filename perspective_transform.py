import numpy as np
import cv2


"""
takes list of four points specifying (x,y) coordinates of each rectangle corner
return array of points
top left, top right, bottom right, bottom left
determined by 
"""
def order_points(pts):
    # initalize list of ordered coordinates
    # 1:top-left, 2:top-right, 3:bottom-right, 4:bottom-left
    rect = np.zeros((4,2), dtype = "float32")

    # top-left smallest sum, top-right, largest sum
    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    # top-right, smallest difference, bottom-left, largest difference
    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect

def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    #compute maxWidth of image
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))    
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))    
    maxWidth = max(int(widthA), int(widthB))

    #compute maxHeight of image
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # construct set of destination points for birds eye view
    dst = np.array([
        [0,0],
        [maxWidth-1, 0],
        [maxWidth-1, maxHeight-1],
        [0, maxHeight-1]], dtype = "float32")

    #compute perspective transform matrix -> apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped

