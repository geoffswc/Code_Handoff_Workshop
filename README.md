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

## Sample Data Preparation

The sample data used is a subset of a Sentiment Polarity Dataset from Cornell.  To access the raw data used for input, visit:

http://www.cs.cornell.edu/people/pabo/movie-review-data/

and download the "polarity dataset v1.0" 

This data is not available in the tab delimited format required by this script. Instead, it is stored as a collection of loose files in a "pos" and "neg" directory. 

This repository contains two scripts to create the tsv files from this directory and file structure.  

prepare_files.py creates a new file, reviews.tsv.  This script reads all negative and positive reviews, extracts the text, and enters the text as a line in reviews.tsv, with an ID and a sentiment score, 0 or 1, based on whether the review came from the positive or negative review directories.

randomize_files shuffles the reviews.tsv file so that the lines alternate randomly between positive and negative revies.  This way, this file can be split into training and testing sets that contain both types of reviews.

## Running the Data Preparation scripts

Download "polarity dataset v.10" into a directory contianing prepare_files.py and randomize.py

from the mix20_rand700_tokens_cleaned/tokens directory, run

prepare_files.py

this will create a new file, reviews.tsv
this file creates one tsv row per review, with an id, category, and text per row.
note that this file will have all non alphanumerical characters stripped out.  You may lose data through this process.  If you want to have other special characters preset, you may want to edit this script (thought this may also require changes to Classifier.py)

the first half of reviews.tsv is negative reviews, the second half is positive reviews.  We will want both types in our training and test set.  

To randomize the lines, type

randomize_files.py

this will randomize the rows.

Now, to split the files into a training and testing set, we can use the unix head and tail methods.

head -500 reviews.tsv > trainRecords.tsv

to get the next 500 records for a test set

tail -700 reviews.tsv | head -500 > testRecords.tsv

The classifier expects a header row, so open these files and write (tab delimited)

id	category	text

as the first line.  

You can now run the Classifier.py script on the trainRecords.tsv and testRecords.tsv file

python Classifier.py trainRecords.tsv testRecords.tsv

If you haven't changed any of the defaults for the Random Forst, you should see an accuracy in the low 60s (note that you can improve this by increasing the n_forests parameter in the script).


