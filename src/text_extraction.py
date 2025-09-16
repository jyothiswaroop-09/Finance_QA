import re
import pandas as pd

class TextExtractor:
    def __init__(self, text):   # <-- FIXED HERE (double underscore)
        self.text = text 

    def parse_table(self):
        rows = []
        for line in self.text.split("\n"):
            parts = line.strip().split()
            if len(parts) >= 4 and parts[0].isdigit():
                year = parts[0]
                values = [p.replace(",", "") for p in parts[1:4]]
                rows.append([year] + values)
        if rows:
            df = pd.DataFrame(rows, columns=["Year", "Revenue", "Expenses", "Profit"])
            return df
        return None

    def extract_revenue(self):
        df = self.parse_table()
        if df is not None:
            return df[["Year", "Revenue"]].to_dict(orient="records")
        match = re.search(r"Revenue[:\-]?\s*\$?([\d,]+)", self.text, re.IGNORECASE)
        return match.group(1) if match else "Not Found"

    def extract_profit(self):
        df = self.parse_table()
        if df is not None:
            return df[["Year", "Profit"]].to_dict(orient="records")
        match = re.search(r"Profit[:\-]?\s*\$?([\d,]+)", self.text, re.IGNORECASE)
        return match.group(1) if match else "Not Found"

    def extract_expenses(self):
        df = self.parse_table()
        if df is not None:
            return df[["Year", "Expenses"]].to_dict(orient="records")
        match = re.search(r"Expenses[:\-]?\s*\$?([\d,]+)", self.text, re.IGNORECASE)
        return match.group(1) if match else "Not Found"