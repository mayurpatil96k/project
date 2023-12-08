import sys
import argparse

import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
      success,image = vidcap.read()
      print ('Read a new frame: ', success)
      #cv2.imwrite( pathOut + "\\frame%d.jpg" % count, image)    
      count += 1

if __name__=="__main__":
    print("aba")
    pathIn = 'C:/Users/Mayur/Desktop/project/video.mp4'
    pathOut = 'C:/Users/Mayur/Desktop/project/output'
    extractImages(pathIn, pathOut)