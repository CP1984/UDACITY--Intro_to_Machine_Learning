#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
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
from sklearn.naive_bayes import GaussianNB
import numpy as np
# Create a Naive Bayes Classifier called clf
clf = GaussianNB()

# Train the classifier the count the training time
timeStartTraining = time()
clf.fit(features_train, labels_train)
timeEndTraining = time()

# Predict the test sample and count the predicting time
timeStartPredicting = time()
predict_test = clf.predict(features_test)
timeEndPredicting = time()

# Print the accuracy, training time and predicting time
print "Accuracy: ", clf.score(features_test, labels_test)
print "Training time:", timeEndTraining - timeStartTraining, "s"
print "Predicting time:", timeEndPredicting - timeStartPredicting, "s"

#########################################################


