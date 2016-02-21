import numpy as np
import glob
import json
from skimage import data
from skimage import io
from skimage import transform as tf
from skimage.feature import (match_descriptors, corner_harris,
                             corner_peaks, ORB, plot_matches)
from skimage.color import rgb2gray

MIN_MATCH_COUNT = 10
paths = glob.glob('./*.jpg')
descriptions = []

# Initiate SIFT detector
descriptor_extractor = ORB(n_keypoints=200)

# find the keypoints and descriptors with SIFT
for path in paths:
    img = io.imread(path, as_grey=True)
    descriptor_extractor.detect_and_extract(img)
    des = descriptor_extractor.descriptors
    descriptions.append(des)

#Make long array
des_array = []
for i in range(len(descriptions)):
        des_array.append(descriptions[i].tolist())
f = open('tempfile','w')
f.write(json.dumps(des_array))
f.close()
