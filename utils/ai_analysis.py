from utils.keyword_extractor import KeywordExtractor
from utils.entity_extractor import EntityExtractor
from utils.summarizer import TextSummarizer


class AIAnalyzer:

    def __init__(self):

        self.keyword = KeywordExtractor()

        self.entity = EntityExtractor()

        self.summary = TextSummarizer()

    def analyze(self, text):

        summary = self.summary.summarize_text(text)

        keywords = self.keyword.extract(text)

        entities = self.entity.extract(text)

        important_points = []

        for line in text.split("\n"):

            line = line.strip()

            if len(line) > 10:

                important_points.append(line)

        return {

            "summary": summary,

            "keywords": keywords,

            "entities": entities,

            "important_points": important_points[:20]

        } 