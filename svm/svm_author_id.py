#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time

sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

from sklearn.svm import SVC
import numpy as np

clf = SVC(kernel="rbf", C=10000.0)
features_train = features_train[int(0):int(len(features_train) / 100)]
labels_train = labels_train[int(0):int(len(labels_train) / 100)]
t0 = time()
clf.fit(features_train, labels_train)
print(round(time() - t0, 3))
# prettyPicture(clf, features_test, labels_test)
# output_image("test.png", "png", open("test.png", "rb").read())
pred = clf.predict(features_test)
a = clf.score(features_test, labels_test)
aa = np.count_nonzero(pred)

print(aa)

#########################################################


