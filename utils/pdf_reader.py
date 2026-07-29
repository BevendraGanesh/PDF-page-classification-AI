"""
pdf_reader.py
-----------------------
Reads PDF files page by page using PyMuPDF.
"""

import fitz


class PDFReader:

    def __init__(self):
        pass

    def read_pdf(self, uploaded_file):
        """
        Read uploaded PDF and return page-wise text.

        Parameters
        ----------
        uploaded_file : UploadedFile

        Returns
        -------
        list
        """

        pdf = fitz.open(
            stream=uploaded_file.read(),
            filetype="pdf"
        )

        pages = []

        for page_number in range(len(pdf)):

            page = pdf.load_page(page_number)

            text = page.get_text()

            pages.append({
                "page_number": page_number + 1,
                "text": text
            })

        pdf.close()

        return pages