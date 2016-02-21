import matplotlib
matplotlib.use('Agg')

import cv2
from collections import Counter
from contextlib import contextmanager
import os
import time
import cPickle


@contextmanager
def Timer(name):
    print "Starting: ", name
    start = time.time()
    yield
    print "{} took {}s".format(name, time.time() - start)



NUM_FEATURES = 256
orb = cv2.ORB(nfeatures=NUM_FEATURES)
bfs = cv2.BFMatcher(cv2.NORM_HAMMING)

test_img = cv2.imread('mona1.jpg', 0)
keypoints_test, description_test = orb.detectAndCompute(test_img, None)

with Timer("creating db"):
    try:
        features, image_to_filename = cPickle.load(open("db.dat"))
        bfs.add(features)
    except Exception, e:
        print e
        image_to_filename = []
        features = []
        for i, img in enumerate(os.listdir("images")):
            print("Loading: ", img)
            image = cv2.imread('images/' + img, 0)
            kp, des = orb.detectAndCompute(image, None)
            if des is not None:
                print "got features"
                image_to_filename.append(img)
                features.append(des)
                bfs.add(des)
        cPickle.dump((features, image_to_filename), open("db.dat", "w+"))

with Timer("matching"):
    matches = bfs.knnMatch(description_test, 2)

with Timer('tallying'):
    # Apply ratio test
    which = Counter()
    for m, n in matches:
        if m.distance > 0.7 * n.distance:
            which[m.imgIdx] += 1


result = [(image_to_filename[pic], score) for pic, score in which.most_common(10)]
print result[:10]
