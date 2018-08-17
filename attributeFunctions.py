import numpy as np
import cv2
from showRed import *
from attObject import * 
from papules import * 

# used parts of showRed and red from https://github.com/VasuAgrawal/112-opencv-tutorial
# No code copy pasted, only understood how to use edge detection and color thresholding i.e only took the idea of lower_red #and upper_red range in showRed functions
    
def koebner(img):
    img = red(img).getImage()
        
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    
    kphenom = Attribute("Koebner Phenomenon",edges)
    return kphenom
    
    
def scaling(img):
    gray1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray1 = cv2.bilateralFilter(gray1, 11, 15, 17)
    edged1 = cv2.Canny(gray1, 10, 200)
    
    scaling = Attribute("Scaling",edged1)
    
    return scaling
    
def showRed(frame):
    lower_red = np.array([4, 120, 110])
    upper_red = np.array([255, 220, 220])
    if frame is not None:
        blurred = cv2.GaussianBlur(frame, (31, 31), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV) #convert to HSV
        mask = cv2.inRange(hsv, lower_red, upper_red) 
        frame = cv2.bitwise_and(frame, frame, mask=mask) 
        
        red1 = Attribute("Erythema",frame)
        return red1

def red(frame):
    lower_red = np.array([0, 110, 50])
    upper_red = np.array([255, 255, 255])
    if frame is not None:
        blurred = cv2.GaussianBlur(frame, (31, 31), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV) #convert to HSV
        mask = cv2.inRange(hsv, lower_red, upper_red) 
        frame = cv2.bitwise_and(frame, frame, mask=mask) 
        
        red2 = Attribute("Erythema",frame)
        return red2
def pap(frame):
    image,number= papules(frame)

    papule = Papules("Papules",image,number)
    return papule
    
"""
img = cv2.imread('/Users/ishaanjaffer/Downloads/k.jpg')

cv2.imshow('edges',papules.getImage())


cv2.waitKey(0)
cv2.destroyAllWindows()"""