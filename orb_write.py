import numpy as np
import cv2
import glob
import json

MIN_MATCH_COUNT = 10
paths = glob.glob('./*.jpg')
descriptions = []

# Initiate SIFT detector
sift = cv2.SIFT()

# find the keypoints and descriptors with SIFT
for path in paths:
    img = cv2.imread(path,0)
    kp, des = sift.detectAndCompute(img,None)
    descriptions.append(des)

#Make long array
des_array = []
for i in range(len(descriptions)):
        des_array.append(descriptions[i].tolist())
f = open('tempfile','w')
f.write(json.dumps(des_array))
f.close()
