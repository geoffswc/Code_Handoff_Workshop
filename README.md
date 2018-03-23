# Code_Handoff_Workshop

## Overview

This repository contains a script to measure the accuracy of a random forest in binary classification of text documents. and applies the random forest model to predict a lcassification for each entry.

The script reads in a tsv file of training and testing text documents.  Each row in the train and test documents contains an id, the body of the text for each entry, and a binary classification (0 or 1).  

The script breaks the training documents in to a bag of words with a maximum of 5000 features, creates word vectors for the training set, and trains a random forest.  

The script then reads in a testing set and applies the random forest model to predict a lcassification for each entry.

Lastly, the algorithm compares the predictions for the test set to the actual categories and calculates an accuracy metric.  This metric is a simple calculation of the number of correct predictions as a percentage of the total.

Note that all scikit-learn parameters for the random forest are left at the scikit defaults. 

## Dependencies

Python 3.6+ (built using 3.6.3)

scikit-learn (built using 0.19.1)

http://scikit-learn.org/stable/install.html

## Input Files

This application requires a test and train file.
Files must be tab delimited.  
The header row contains id, category, and text

id contains an identifier for the data row

category contains a numerical representation of the category for an item.
note that the script assumes binary representation categories (0 or 1). 

text contains the raw text for the item to be categorized.

## Sample Data

Sample Data is available in the data directory.  

This data set contains text for movie reviews, categorized 0 (negative) or 1 (positive),
split into training and testing data sets.  

## to run the application with the sample data, run:

python Classifier.py data/trainReviews.tsv data/testReviews.tsv


