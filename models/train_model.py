"""
train_model.py
----------------------------------------
Train PDF Page Classification Model
"""

import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from utils.preprocessing import TextPreprocessor
from utils.feature_extraction import FeatureExtractor
from utils.classifier import PDFClassifier


# -----------------------------
# Dataset Path
# -----------------------------

DATASET_PATH = "dataset/train"


# -----------------------------
# Read Dataset
# -----------------------------

texts = []
labels = []

for category in os.listdir(DATASET_PATH):

    category_path = os.path.join(DATASET_PATH, category)

    if not os.path.isdir(category_path):
        continue

    for file in os.listdir(category_path):

        if file.endswith(".txt"):

            file_path = os.path.join(category_path, file)

            with open(file_path, "r", encoding="utf-8") as f:

                text = f.read()

                texts.append(text)

                labels.append(category)


print(f"Total Documents : {len(texts)}")


# -----------------------------
# Text Preprocessing
# -----------------------------

preprocessor = TextPreprocessor()

clean_texts = []

for text in texts:

    clean_texts.append(
        preprocessor.clean_text(text)
    )


# -----------------------------
# Feature Extraction
# -----------------------------

extractor = FeatureExtractor()

X = extractor.fit_transform(clean_texts)

y = labels


# -----------------------------
# Train Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# -----------------------------
# Train Classifier
# -----------------------------

classifier = PDFClassifier()

classifier.train(X_train, y_train)


# -----------------------------
# Prediction
# -----------------------------

predictions = classifier.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"Accuracy : {accuracy*100:.2f}%")

# -----------------------------
# Save Model
# -----------------------------

os.makedirs("saved_models", exist_ok=True)

classifier.save(
    "saved_models/model.pkl"
)

extractor.save(
    "saved_models/vectorizer.pkl"
)

print("Model Saved Successfully.")