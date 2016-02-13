import numpy as np
import cv2
import json
import glob
import sys

MIN_MATCH_COUNT = 10
paths = glob.glob('./*.jpg')

#Initiate Flann procedure
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

# Initiate SIFT detector
sift = cv2.SIFT()

#Read in File
with open('tempfile') as data_file:
        descriptions_reborn = json.load(data_file)

for i in range(len(descriptions_reborn)):
        descriptions_reborn[i] = np.asarray(descriptions_reborn[i], dtype=np.float32)

#Check against other images
test_img = cv2.imread('test/aataco1.jpg',0)
kp, test = sift.detectAndCompute(test_img,None)
a = 0
found = False
for ind,description in enumerate(descriptions_reborn):
    good = []
    matches = flann.knnMatch(test,description,k=2)
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)
        if len(good) > MIN_MATCH_COUNT:
            found = True
    if found:
        a = 1
        break

print a
