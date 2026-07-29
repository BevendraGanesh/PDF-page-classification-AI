"""
preprocessing.py
-----------------------
Text preprocessing functions.
"""

import re


class TextPreprocessor:

    def __init__(self):
        pass

    def clean_text(self, text):
        """
        Clean extracted text.
        """

        # Convert to lowercase
        text = text.lower()

        # Remove numbers
        text = re.sub(r"\d+", " ", text)

        # Remove punctuation
        text = re.sub(r"[^\w\s]", " ", text)

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        return text.strip()