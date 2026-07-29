import os
import pandas as pd
from sklearn.model_selection import train_test_split

from utils.preprocessing import TextPreprocessor
from utils.feature_extraction import FeatureExtractor
from utils.classifier import PDFClassifier

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("dataset/dataset.csv")
print(df["label"].value_counts())

texts = df["text"].astype(str)
labels = df["label"].astype(str)

# -----------------------------
# Preprocess Text
# -----------------------------
preprocessor = TextPreprocessor()

clean_texts = []

for text in texts:
    clean_texts.append(preprocessor.clean_text(text))

# -----------------------------
# Feature Extraction
# -----------------------------
extractor = FeatureExtractor()

X = extractor.fit_transform(clean_texts)
y = labels

# -----------------------------
# Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
classifier = PDFClassifier()

classifier.train(X_train, y_train)

from sklearn.metrics import accuracy_score, classification_report

y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

print(classification_report(y_test, y_pred))

# -----------------------------
# Create Folder
# -----------------------------
os.makedirs("saved_models", exist_ok=True)

# -----------------------------
# Save Files
# -----------------------------
extractor.save("saved_models/vectorizer.pkl")
classifier.save("saved_models/model.pkl")

print("===================================")
print("Training Completed Successfully")
print("Files Saved:")
print("saved_models/vectorizer.pkl")
print("saved_models/model.pkl")
print("===================================")