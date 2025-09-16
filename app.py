import streamlit as st
from src.document_loader import DocumentLoader
from src.text_extraction import TextExtractor
from src.nlp_processor import NLPProcessor
from src.utils import save_uploaded_file

st.set_page_config(page_title="Financial Document Q&A", layout="wide")
st.title("📊 Financial Document Question-Answering System")

uploaded_file = st.file_uploader("Upload a PDF or Excel file", type=["pdf", "xlsx"])

if uploaded_file:
    # Save file
    file_path = save_uploaded_file(uploaded_file)

    # Load content
    loader = DocumentLoader(file_path)
    if uploaded_file.type == "application/pdf":
        text = loader.load_pdf()
    else:
        text = loader.load_excel()

    # Show preview
    st.subheader("📑 Extracted Text Preview")
    st.text_area("Document Content", text[:2000], height=200)

    # -------------------------
    # Quick Extracted Metrics
    # -------------------------
    extractor = TextExtractor(text)
    df = extractor.parse_table()

    st.subheader("📌 Quick Extracted Metrics")
    if df is not None:
        st.dataframe(df)  # show full extracted table
    else:
        st.warning("No structured table could be extracted from the document.")

    # -------------------------
    # Q&A Section
    # -------------------------
    st.subheader("💬 Ask Questions about Financial Data")
    question = st.text_input("Enter your question:")

    if st.button("Get Answer") and question:
        nlp = NLPProcessor()
        answer = nlp.ask(question, text)
        st.success(answer)