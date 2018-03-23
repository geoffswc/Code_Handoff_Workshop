from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import sys

train = pd.read_csv(sys.argv[1], header=0, delimiter="\t", quoting=3)

vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = 'english',   \
                             max_features=5000)

train_data_features = vectorizer.fit_transform(train["text"])

clf = RandomForestClassifier()

clf.fit( train_data_features, train["category"] )

test = pd.read_csv(sys.argv[2], header=0, delimiter="\t", quoting=3)

test_data_features = vectorizer.transform(test['text'])

binary_predictions = clf.predict(test_data_features)

prediction_list = pd.DataFrame( data={"id":test["id"], "category":test['category'], "prediction":binary_predictions} )

# calculate accuracy as a percentage of binary predictions that were correct
print(1 - (sum(np.absolute(prediction_list['category'] - prediction_list['prediction'])) / len(prediction_list['prediction'])))


