import os
import urllib.request

import joblib
import nltk
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download("stopwords")
# loads the dataset as a dataframe
df = pd.read_csv("airline_sentiment_analysis.csv", encoding="utf-8")


tokenizer = RegexpTokenizer(r"\w+")
en_stopwords = set(stopwords.words("english"))
ps = PorterStemmer()


def processReview(review):
    """The module does the following jobs:
    1 - Converts reviews to lower case
    2 - Removes the HTML tags and # s that are common in tweets
    3 - Breaking them into tokens and retaining them if they are not stopwords
    4 - Stemming the reviews to root words
    """
    review = review.lower()
    review = review.replace("<br /><br />", " ")
    review = review.replace("#", " ")
    # Tokenize
    tokens = tokenizer.tokenize(review)
    new_tokens = [token for token in tokens if token not in en_stopwords]
    stemmed_tokens = [ps.stem(token) for token in new_tokens]
    clean_review = " ".join(stemmed_tokens)
    return clean_review


# Applying the
df["text"].apply(processReview)
# Splitting the data for training and testing
X_train = df.loc[:9500, "text"].values
y_train = df.loc[:9500, "airline_sentiment"].values
X_test = df.loc[2000:, "text"].values
y_test = df.loc[2000:, "airline_sentiment"].values

# Vectorizing the words i.e. converting them to numerical form.
vectorizer = TfidfVectorizer(sublinear_tf=True, encoding="utf-8", decode_error="ignore")
# Passing the training data to vectorizer
vectorizer.fit(X_train)
X_train = vectorizer.transform(X_train)
""" Passing the test data as well to the vectorizer. Fitting is only needed for training as the same model is used 
 later for testing """
X_test = vectorizer.transform(X_test)

# Applying logistic regression algorithm for training
model = LogisticRegression(solver="liblinear")
model.fit(X_train, y_train)
print("Score on training data is: " + str(model.score(X_train, y_train)))
print("Score on testing data is: " + str(model.score(X_test, y_test)))

# Saving the models for future use
joblib.dump(en_stopwords, "nlpmodels/stopwords.pkl")
joblib.dump(model, "nlpmodels/model.pkl")
joblib.dump(vectorizer, "nlpmodels/vectorizer.pkl")
