import cv2
import numpy as np
from matplotlib import pyplot as plt

import decimal
#round Half Up taken from 112 notes
def roundHalfUp(d):
    
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))
class Attribute(object):
    def __init__(self,name,image):
        self.name = name 
        self.image = image 
    
    def getImage(self):
        return self.image
    def getName(self):
        return self.name 
    def scalingValue(self):
        value=0
        nonBlack = np.count_nonzero(self.image)
        total = self.image.size 
        black = total - nonBlack
        ratio = roundHalfUp(nonBlack*100/black)
        if(ratio<4):
            value=0
        elif(ratio<10):
            value = 1
        elif(ratio<13):
            value = 2
        elif(ratio<16):
            value = 2
        else:
            value = 3
        return (value)
    def kPhenomValue(self):
        value=0
        nonBlack = np.count_nonzero(self.image)
        total = self.image.size 
        black = total - nonBlack
        ratio = (nonBlack*100/black)
        
        if ratio>=10:# extreme edge case when there is sccaling throughout, leads to a wrong ratio 
            value = 1
        elif ratio>=3:
            value = 3
        elif ratio>=1.2:
            value = 2 
        elif(ratio>=0.5):
            value = 1
        else:
            value = 0
        return value 
    def redRatio(self):
        value = 0
        nonBlack = np.count_nonzero(self.image)
        total = self.image.size 
        black = total - nonBlack
        ratio = (nonBlack*100/black)
        return ratio 
    def eryValue(self):
        value = 0
        nonBlack = np.count_nonzero(self.image)
        total = self.image.size 
        black = total - nonBlack
        ratio = (nonBlack*100/black)
        
        if(ratio>200):# in case skin is evenly red all throughout 
            value =1
        elif(ratio>=10):
            value = 3 #max red 
        elif(ratio>3):
            value =  2
        elif(ratio>0.5):
            value = 1
        else:
            value = 0
            
        
        return value
class Papules(Attribute):
    def __init__(self,name,image,number):
        super().__init__(name,image) # call overridden init!
        self.number = number
    
    def papValue(self):
        value = 0
        if(self.number>=50):
            value = 3
        elif(self.number>=18):
            value = 2
        elif(self.number>=10):
            value = 1
        else:
            value = 0
            
        return value 
    

    
 
    

        
    
   
    
    
    
    
   


    