# Code_Handoff_Workshop

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


