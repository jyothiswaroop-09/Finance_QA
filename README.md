# 📊 Financial Document Q&A Assistant

An interactive **web application** built with **Streamlit** that allows users to upload financial documents (**PDF** or **Excel**) and ask natural language questions about key financial metrics such as **revenue, profit, and expenses**.  

This project demonstrates **document processing, text extraction, and NLP-powered Q&A** using **Ollama with local Small Language Models (SLMs)**.

---

## 🎯 Problem Statement
Develop a web application that can process financial documents (PDF and Excel formats) and provide an interactive **question-answering system** for users to query financial data using natural language.

The application should:
- Extract relevant financial information from uploaded documents  
- Respond to user questions about revenue, expenses, profits, and other financial metrics  
- Provide a clean and interactive user interface  

---

## 📋 Features
### 🔹 Document Processing
- Upload **PDF** and **Excel** financial documents  
- Extract **text** and **numerical data** from:
  - Income statements  
  - Balance sheets  
  - Cash flow statements  
- Handle different layouts and formats  

### 🔹 Question-Answering
- Ask questions like:
  - *"What is the total revenue?"*  
  - *"How much profit did the company make?"*  
  - *"List the expenses from the financial report."*  
- Uses **NLP** for interpreting queries  
- Powered by **Ollama (local SLMs)**  

### 🔹 User Interface
- Built with **Streamlit**  
- File upload widget for PDFs and Excel  
- Preview of extracted text (first 2000 characters)  
- Display of **quick metrics** (revenue, profit, expenses)  
- Chat-style **Q&A interaction**  

---

## 🛠️ Tech Stack
- **Python 3.10+**  
- **Streamlit** – Web interface  
- **PyMuPDF** – PDF text extraction  
- **Pandas** – Excel data parsing  
- **Regex** – Financial metric extraction  
- **Ollama** – Local Small Language Models (LLMs/SLMs) for Q&A  

---

## 🚀 Setup Instructions

1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/financial-qna-assistant.git
cd financial-qna-assistant

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install Ollama
ollama pull llama3

5️⃣ Run Application
streamlit run app.py
```
### 📂 Project Structure
```
financial-qna-assistant/
│
├── app.py                     # Streamlit app entry point
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
│
├── src/
│   ├── __init__.py
│   ├── document_loader.py     # PDF & Excel document loading
│   ├── text_extraction.py     # Regex-based metric extraction
│   ├── nlp_processor.py       # Q&A with Ollama models
│   ├── utils.py               # Helper functions (file saving, etc.)
```
## 🖥️ Usage

Run the app using streamlit run app.py
Upload a PDF or Excel financial statement
Preview extracted content
See quick financial metrics (revenue, profit, expenses)
Ask natural language questions in the chat box

