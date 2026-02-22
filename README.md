# 🧠 AI Personal Research Assistant

An intelligent research automation tool that searches the web, extracts content, summarizes information, and generates structured reports — all from a single research question.

---

## 📌 Overview

**AI Personal Research Assistant** is an LLM-powered application that automates the research process. Instead of manually reading multiple articles, the system:

1. Searches relevant sources online
2. Extracts meaningful content
3. Summarizes each document
4. Generates a structured final report

This project demonstrates real-world usage of:

* Retrieval-Augmented Generation (RAG)
* Prompt Engineering
* LLM Pipelines
* AI Workflow Orchestration

---

## 🚀 Features

✔ Accepts any research question
✔ Retrieves live web sources
✔ Extracts clean text from URLs
✔ Summarizes each source separately
✔ Generates professional research report
✔ Structured output format
✔ Interactive Streamlit UI

---

## 🧠 System Architecture

User Question
→ Web Search (Tavily)
→ URL Extraction
→ Content Extraction Prompt
→ Summarization Prompt
→ Report Generation Prompt
→ Final Structured Report

---

## 🛠 Tech Stack

| Tool          | Purpose           |
| ------------- | ----------------- |
| Streamlit     | Frontend UI       |
| LangChain     | LLM orchestration |
| Google Gemini | Language Model    |
| Tavily API    | Web Search        |
| Python        | Backend logic     |

---

## 📂 Project Structure

```
ai-personal-research-assistant/
│── app.py
│── requirements.txt
│── .env
│── README.md
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repo

```
git clone <repo-url>
cd ai-personal-research-assistant
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Setup API Keys

Create `.env` file:

```
GOOGLE_API_KEY=your_key
TAVILY_API_KEY=your_key
```

---

### 4️⃣ Run App

```
streamlit run app.py
```

---

## 🧪 Example Query

```
How can RAG architectures reduce hallucinations in LLMs?
```

Output → Full research report with insights.

---

## 🎯 Use Cases

* Academic research
* Technical analysis
* Market research
* Competitive analysis
* Literature review
* Rapid learning

---

## ⚠️ Limitations

* Dependent on search API results
* Cannot access paywalled content
* LLM responses may vary slightly

---

## 🔮 Future Improvements

* PDF export
* Chat history memory
* Multi-language support
* Source credibility scoring
* Citation generation
* Streaming responses

---

## 🏆 Learning Outcomes

This project demonstrates understanding of:

* Prompt design
* LLM chaining
* AI system architecture
* Structured output generation
* Real-time data pipelines

---

## 👨‍💻 Author

**Vinay**
AI Developer | LLM Engineer | Agentic AI Enthusiast

---

## ⭐ Contribution

Pull requests and suggestions are welcome!

---

## 📜 License

MIT License
