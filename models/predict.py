"""
predict.py
-----------------------------------
Predict document class from uploaded PDF
"""

from utils.pdf_reader import PDFReader
from utils.preprocessing import TextPreprocessor
from utils.feature_extraction import FeatureExtractor
from utils.classifier import PDFClassifier
from utils.ai_analysis import AIAnalyzer


class PDFPredictor:

    def __init__(self):

        self.reader = PDFReader()
        self.preprocessor = TextPreprocessor()
        self.extractor = FeatureExtractor()
        self.classifier = PDFClassifier()
        self.ai = AIAnalyzer()

        # Load saved model
        self.extractor.load("saved_models/vectorizer.pkl")
        self.classifier.load("saved_models/model.pkl")

    def predict(self, uploaded_file):

        pages = self.reader.read_pdf(uploaded_file)

        results = []

        for page in pages:

            clean_text = self.preprocessor.clean_text(
                page["text"]
            )
            analysis = self.ai.analyze(clean_text)
            features = self.extractor.transform(
                [clean_text]
            )

            prediction = self.classifier.predict(
                features
            )[0]

        probability = self.classifier.predict_proba(features)[0]

        confidence = max(probability) * 100

        results.append({

    "page_number": page["page_number"],

    "prediction": prediction,

    "confidence": round(confidence, 2),

    "summary": analysis["summary"],
 
    "keywords": analysis["keywords"],

    "entities": analysis["entities"],

    "important_points": analysis["important_points"]

            })

        return results