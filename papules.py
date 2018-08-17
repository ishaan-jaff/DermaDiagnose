#basic usage taken from openCv documentation https://docs.opencv.org/2.4/doc/tutorials
# Setup SimpleBlobDetector parameters.
# did not use code,  but rather used documentation to understand the parameters of the blobDetector.
import cv2
import numpy as np;

# Read image

def papules(image):
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()
    
  
    params.minThreshold = 0
    params.maxThreshold = 95
    
    
   
    params.filterByArea = True
    params.minArea = 2
    
    
    params.filterByCircularity = True
    params.minCircularity = 0.1
    
    # Filter by Convexity
    params.filterByConvexity = True
    #params.minConvexity = 
        
    
    params.filterByInertia = True
    params.minInertiaRatio = 0.01
    
    # Create a detector with the parameters
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
        detector = cv2.SimpleBlobDetector(params)
    else : 
        detector = cv2.SimpleBlobDetector_create(params)
    
    
    # Detect blobs.
    keypoints = detector.detect(image)
    
   
    number = (len(keypoints))
    
    im_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    
    # Show blobs
    return (im_with_keypoints,number)

"""frame = cv2.imread("/Users/ishaanjaffer/Downloads/kk.jpeg")
cv2.imshow("Image",papules(frame))
cv2.waitKey(0)
cv2.destroyAllWindows()"""

