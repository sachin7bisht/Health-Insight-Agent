import os

def validate_pdf_file(pdf_file):
    try:
        if not pdf_file.name.lower().endswith('.pdf'):
            return False
        pdf_file.seek(0,os.SEEK_END)
        size_mb=pdf_file.tell()/(1024*1024)
        pdf_file.seek(0)
        if size_mb>5:
            return False
        return True,None
    except Exception as e:
        return False,f'Error file {str(e)}'

def validate_pdf_content(text):
    if not text or len(text.strip())<50:
        return False,"File is empty"
    return True,None