from summa.summarizer import summarize

class TextSummarizer:

    def summarize_text(self, text):

        try:

            result = summarize(
                text,
                ratio=0.25
            )

            if result.strip():

                return result

        except:

            pass

        return text[:400]