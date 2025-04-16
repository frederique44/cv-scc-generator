tests/test_extractors.py
import pytest
from utils.extractors import extract_text, _clean_text
from io import BytesIO
import docx
import pdfplumber
import os

@pytest.fixture
def sample_docx(tmp_path):
    doc = docx.Document()
    doc.add_paragraph("Test DOCX Content")
    path = tmp_path / "test.docx"
    doc.save(path)
    return path

@pytest.fixture
def sample_pdf(tmp_path):
    path = tmp_path / "test.pdf"
    with pdfplumber.open(BytesIO()) as pdf:
        pdf.pages[0].extract_text = lambda: "Test PDF Content"
        pdf.save(path)
    return path

def test_clean_text():
    assert _clean_text("  Hello   World  ") == "Hello World"
    assert _clean_text("• Item1\n•Item2") == "• Item1\n•Item2"

def test_extract_docx(sample_docx):
    with open(sample_docx, "rb") as f:
        text = extract_text(f)
        assert "Test DOCX Content" in text

def test_extract_pdf(sample_pdf):
    with open(sample_pdf, "rb") as f:
        text = extract_text(f)
        assert "Test PDF Content" in text
