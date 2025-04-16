utils/extractors.py
import pdfplumber
from docx import Document
import io

def extract_text(file):
    """Extrait le texte brut depuis PDF ou DOCX"""
    if file.type == "application/pdf":
        with pdfplumber.open(io.BytesIO(file.read())) as pdf:
            return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    else:
        doc = Document(io.BytesIO(file.read()))
        return "\n".join([para.text for para in doc.paragraphs])
