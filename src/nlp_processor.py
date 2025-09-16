import re
from src.text_extraction import TextExtractor

class NLPProcessor:
    def ask(self, question, text):
        extractor = TextExtractor(text)
        df = extractor.parse_table()

        q = question.lower()
        if df is not None:
            year_match = re.search(r"(20\d{2})", q)
            year = year_match.group(1) if year_match else None

            if "revenue" in q:
                if year:
                    row = df[df["Year"] == year]
                    if not row.empty:
                        return f"Revenue in {year} was {row['Revenue'].values[0]}"
                return f"Available revenues: {df[['Year','Revenue']].to_dict(orient='records')}"

            elif "profit" in q:
                if year:
                    row = df[df["Year"] == year]
                    if not row.empty:
                        return f"Profit in {year} was {row['Profit'].values[0]}"
                return f"Available profits: {df[['Year','Profit']].to_dict(orient='records')}"

            elif "expense" in q:
                if year:
                    row = df[df["Year"] == year]
                    if not row.empty:
                        return f"Expenses in {year} were {row['Expenses'].values[0]}"
                return f"Available expenses: {df[['Year','Expenses']].to_dict(orient='records')}"

        return "Sorry, I could not find relevant financial information."