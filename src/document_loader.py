# src/document_loader.py
import pandas as pd
import fitz  # PyMuPDF for PDF reading

class DocumentLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_pdf(self) -> str:
        """Extract text from a PDF file."""
        text = ""
        try:
            with fitz.open(self.file_path) as doc:
                for page in doc:
                    text += page.get_text("text")
        except Exception as e:
            text = f"Error reading PDF: {e}"
        return text

    def load_excel(self) -> str:
        """Extract text from an Excel file (concatenate sheet values)."""
        text = ""
        try:
            xls = pd.ExcelFile(self.file_path)
            for sheet in xls.sheet_names:
                df = xls.parse(sheet)
                text += df.to_string(index=False)
                text += "\n\n"
        except Exception as e:
            text = f"Error reading Excel: {e}"
        return text
