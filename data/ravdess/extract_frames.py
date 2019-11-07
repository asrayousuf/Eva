import os
import sys
import argparse
import cv2

def extractImages(pathIn):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
        success,image = vidcap.read()
        if not success:
            break
        cv2.imwrite("{}-{}.jpg".format(pathIn[:-4], count), image)
        count = count + 1

if __name__=="__main__":
    for filename in os.listdir('.'):
        if filename.endswith('.mp4'):
            extractImages(filename)
            print('done extracting images for {}'.format(filename))
