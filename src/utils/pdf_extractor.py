import pdfplumber
from PIL import Image
import pytesseract
import io
import os
from utils.validators import validate_pdf_content,validate_pdf_file


def extract_text_from_pdf(pdf_file):
    try:
        is_valid,error=validate_pdf_file(pdf_file)
        if not is_valid:
            return error
        text=''
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                extracted=page.extract_text()
                if not extracted:
                    return 'Cound not extracted text from PDF.'
                text+=extracted+'\n'
        is_valid,error=validate_pdf_content(text)

        if not is_valid:
            return error
        return text
    except Exception as e:
        return f"Error extractimg text {str(e)}"
