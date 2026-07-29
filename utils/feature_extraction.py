"""
feature_extraction.py
----------------------------
Convert text into numerical features using TF-IDF.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import joblib


class FeatureExtractor:

    def __init__(self):

        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=5000
        )

    def fit_transform(self, texts):
        """
        Train vectorizer on training data.
        """

        features = self.vectorizer.fit_transform(texts)

        return features

    def transform(self, texts):
        """
        Convert new text using trained vectorizer.
        """

        return self.vectorizer.transform(texts)

    def save(self, path):
        """
        Save vectorizer.
        """

        joblib.dump(self.vectorizer, path)

    def load(self, path):
        """
        Load saved vectorizer.
        """

        self.vectorizer = joblib.load(path)