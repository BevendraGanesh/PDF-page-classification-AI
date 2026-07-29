import yake


class KeywordExtractor:

    def __init__(self):

        self.extractor = yake.KeywordExtractor(
            lan="en",
            n=2,
            top=10
        )

    def extract(self, text):

        keywords = self.extractor.extract_keywords(text)

        return [k[0] for k in keywords]