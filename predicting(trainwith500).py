# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score

# Load dataset containing political headlines and sentiments
dataFrame = pd.read_csv('Headlines of Politics(Training Data).csv')

# Check for NaN values in the 'sentiment' column and remove rows with NaN values
dataFrame = dataFrame.dropna(subset=['sentiment'])

# Define feature (headlines) and target variable (sentiment)
X = dataFrame['Headlines']
y = dataFrame['sentiment']

# Split the data into training and test sets (70% training, 30% testing)
trainX, testX, trainy, testy = train_test_split(X, y, shuffle=True, train_size=0.7)

# Pipeline for Count Vectorizer with Naive Bayes classifier
modelCount = make_pipeline(CountVectorizer(), MultinomialNB())
# Train the model with the training data
modelCount.fit(trainX, trainy)
# Make predictions on the test data
predictedY = modelCount.predict(testX)
# Calculate accuracy for Count Vectorizer model
accuracy = accuracy_score(predictedY, testy)
print('Accuracy using Count Vectorizer and Multinomial Naive Bayes is', accuracy * 100)

# Pipeline for Tfidf Vectorizer with Naive Bayes classifier
modelTfidf = make_pipeline(TfidfVectorizer(), MultinomialNB())
# Train the model with the training data
modelTfidf.fit(trainX, trainy)
# Make predictions on the test data
predictedY2 = modelTfidf.predict(testX)
# Calculate accuracy for Tfidf Vectorizer model
accuracy2 = accuracy_score(predictedY2, testy)
print('Accuracy using Tfidf and Multinomial Naive Bayes is', accuracy2 * 100)

# Load new dataset for prediction (testing set without labeled sentiments)
testingSetData = pd.read_csv('Last 24 Hours News(Testing Datanew).csv')
# Extract headlines from the new dataset
testingSetHeadline = testingSetData['Headlines']

# Predict sentiments using the Count Vectorizer model
predictedValues = modelCount.predict(testingSetHeadline)
# Predict sentiments using the Tfidf Vectorizer model
predictedValues2 = modelTfidf.predict(testingSetHeadline)

# Create DataFrames for storing predictions from each model
dfPredictedC = pd.DataFrame({'Headlines': testingSetHeadline, 'Sentiment': predictedValues})
dfPredictedT = pd.DataFrame({'Headlines': testingSetHeadline, 'Sentiment': predictedValues2})

# Display the predictions
print(dfPredictedC)
print(dfPredictedT)
