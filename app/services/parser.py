from typing import Optional
import os
from PyPDF2 import PdfReader


def parse_pdf_resume(file_path: str) -> Optional[str]:
    if not os.path.exists(file_path):
        return None

    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        print(f"[ERROR] Failed to parse PDF: {e}")
        return None