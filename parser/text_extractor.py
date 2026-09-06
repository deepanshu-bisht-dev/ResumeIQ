"""
Extracts raw text from uploaded resume files (PDF or DOCX).
"""

import pdfplumber
import docx


def extract_text(filepath: str, extension: str) -> str:
    """
    Extracts and returns plain text from a PDF or DOCX file.
    """
    if extension == "pdf":
        return _extract_from_pdf(filepath)
    elif extension == "docx":
        return _extract_from_docx(filepath)
    else:
        raise ValueError(f"Unsupported file type: {extension}")


def _extract_from_pdf(filepath: str) -> str:
    text_parts = []
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text_parts.append(page_text)
    return "\n".join(text_parts)


def _extract_from_docx(filepath: str) -> str:
    document = docx.Document(filepath)
    return "\n".join(paragraph.text for paragraph in document.paragraphs)
