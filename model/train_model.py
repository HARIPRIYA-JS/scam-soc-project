import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

data = pd.read_csv('dataset/scam_data.csv')

X = data['message']
y = data['label']

model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])

model.fit(X, y)

joblib.dump(model, 'scam_detector.pkl')

print("Model Trained")
