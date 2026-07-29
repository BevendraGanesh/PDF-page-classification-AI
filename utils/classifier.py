import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


class PDFClassifier:

    def __init__(self):
        self.model = LogisticRegression(
            max_iter=1000,
            random_state=42
        )

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)

    def evaluate(self, X_test, y_test):
        prediction = self.predict(X_test)

        print("Accuracy :", accuracy_score(y_test, prediction))
        print(classification_report(y_test, prediction))

    def save(self, path):
        joblib.dump(self.model, path)

    def load(self, path):
        self.model = joblib.load(path)