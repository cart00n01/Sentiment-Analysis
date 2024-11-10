import numpy as np
import pandas as pd

# Load the training data
dataframe = pd.read_csv('Headlines of Politics(Training Data).csv')

# Separate the input (X) and output (y) variables
X = dataframe['Headlines']  # Features (headlines text)
y = dataframe['sentiment']  # Target variable (sentiment)

# Split the data into training and testing sets (70% training, 30% testing)
from sklearn.model_selection import train_test_split
trainX, testX, trainy, testy = train_test_split(X, y, shuffle=2, train_size=0.7)

# Importing CountVectorizer and TfidfVectorizer for text vectorization and Multinomial Naive Bayes for classification
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB

# Build a pipeline for CountVectorizer with MultinomialNB model
modelCount = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model using the training data
modelCount.fit(trainX, trainy)

# Predict sentiments for the test set
predictedY = modelCount.predict(testX)

# Calculate and print the accuracy for the CountVectorizer model
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(predictedY, testy)
print('Accuracy using Count Vectorizer and Multinomial Naive Bayes is', accuracy * 100)

# Optional cross-validation score code (commented out)
# from sklearn.model_selection import cross_val_score
# cross_val_score = cross_val_score(modelCount, X, y, cv=5)
# print(np.array(cross_val_score).mean() * 100)

# Build a pipeline for TfidfVectorizer with MultinomialNB model
modelTfidf = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the Tfidf model using the training data
modelTfidf.fit(trainX, trainy)

# Predict sentiments for the test set using Tfidf model
predictedY2 = modelTfidf.predict(testX)

# Calculate and print the accuracy for the TfidfVectorizer model
accuracy2 = accuracy_score(predictedY2, testy)
print('Accuracy using Tfidf Vectorizer and Multinomial Naive Bayes is', accuracy2 * 100)

# Load the testing dataset
testingSetData = pd.read_csv('Last 24 Hours News(Testing Datanew).csv')
testingSetHeadline = testingSetData['Headlines']  # Only the headlines column is needed

# Predict sentiments on new data using both models
predictedValues = modelCount.predict(testingSetHeadline)  # Using CountVectorizer model
predictedValues2 = modelTfidf.predict(testingSetHeadline)  # Using TfidfVectorizer model

# Display predicted sentiments for each model
print(predictedValues)
print(predictedValues2)

# Create DataFrames for the results
dfPredictedT = pd.DataFrame({'Headlines': testingSetHeadline, 'Sentiment': predictedValues2})  # Tfidf results
dfPredictedC = pd.DataFrame({'Headlines': testingSetHeadline, 'Sentiment': predictedValues})   # CountVectorizer results

# Display the DataFrames
print(dfPredictedC)
print(dfPredictedT)
