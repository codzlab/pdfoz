# backend/pdf_parser.py
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file_path):
    """
    Extract text from a PDF file.

    Args:
        pdf_file_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    text = ""
    try:
        with open(pdf_file_path, "rb") as file:
            pdf_reader = PdfReader(file)
            num_pages = len(pdf_reader.pages)
            for page_num in range(num_pages):
                text += pdf_reader.pages[page_num].extract_text()
    except Exception as e:
        print("Error parsing PDF:", str(e))
    
    return text.strip()
