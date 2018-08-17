import numpy as np
import cv2
from matplotlib import pyplot as plt
import decimal
from attObject import * 
from attributeFunctions import *
# roundHalfUp taken from 112 notes 
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))
    
def showAttributes(ery,scaling,kphenom,polyPap):
    
    titles = [ery.getName(),scaling.getName(),kphenom.getName(),polyPap.getName()]
    images=[ery.getImage(),scaling.getImage(),kphenom.getImage(),polyPap.getImage()]
    values = [ery.eryValue(),scaling.scalingValue(),kphenom.kPhenomValue(),polyPap.papValue()]
    
    
    
        
        
        
    
    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i])
        plt.title(titles[i]+" " + str(values[i]))
        plt.xticks([]),plt.yticks([])
    return plt.show()

def values(ery,scaling,kphenom,polyPap):
    values = [ery.eryValue(),scaling.scalingValue(),kphenom.kPhenomValue(),polyPap.papValue()]
    return values
    