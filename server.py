from flask import Flask, request
import numpy as np
from skimage import data
from skimage import io
from skimage import transform as tf
from skimage.feature import (match_descriptors, corner_harris,
                             corner_peaks, ORB, plot_matches)
import json
import glob
import sys
import pdb
app = Flask(__name__)
app.debug = True

def check_everything():
    MIN_MATCH_COUNT = 30
    paths = glob.glob('./*.jpg')
    
    # Initiate SIFT detector
    descriptor_extractor = ORB(n_keypoints=200)
    
    #Read in File
    with open('tempfile') as data_file:
            descriptions_reborn = json.load(data_file)
    
    for i in range(len(descriptions_reborn)):
            descriptions_reborn[i] = np.asarray(descriptions_reborn[i], dtype=np.float32)
    
    #Check against other images
    img = io.imread('test/aataco1.jpg', as_gray=True)
    descriptor_extractor.detect_and_extract(img,None)
    main_descriptor = descriptor_extractor.descriptors
    a = 0
    found = False
    for ind,description in enumerate(descriptions_reborn):
        good = []
        matches = match_descriptors(main_descriptor, description, cross_check=True)
        pdb.set_trace()
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                good.append(m)
            if len(good) > MIN_MATCH_COUNT:
                return paths[ind] + (" %d" % len(good))
    return "Not Found"

@app.route("/", methods=['GET'])
def hello():
        return "Hello world"

@app.route("/submit/", methods=['POST'])
def getrequest():
        f = open('test/aataco1.jpg','w')
        f.write(request.files['webcam'].getvalue())
        f.close()
        thing = str(check_everything())
        return thing

if __name__ == "__main__":
        app.run(host='0.0.0.0')
