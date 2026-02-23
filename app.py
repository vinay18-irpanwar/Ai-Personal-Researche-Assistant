import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# =========================
# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Personal Research Assistant",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Personal Research Assistant")
st.markdown("Ask any research question and get a structured AI-generated report from live web sources.")

# =========================
# API KEYS
# =========================
GOOGLE_API_KEY = st.sidebar.text_input("Google API Key", type="password")
TAVILY_API_KEY = st.sidebar.text_input("Tavily API Key", type="password")

if not GOOGLE_API_KEY or not TAVILY_API_KEY:
    st.warning("Please enter API keys in sidebar")
    st.stop()

# =========================
# LLM + SEARCH SETUP
# =========================
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY
)

search_tool = TavilySearch(
    result="general",
    max_results=5,
    tavily_api_key=TAVILY_API_KEY
)

parser = StrOutputParser()

# =========================
# PROMPTS
# =========================

extract_prompt = PromptTemplate(
    template="""
You are a precise web content extraction assistant.

Extract main text from each URL.

Rules:
- Ignore ads/nav/footer
- Keep headings
- No summaries
- Separate each URL
- If failed → "Content not accessible"

Return Python list:
["doc1","doc2"]

URLs:
{urls}
""",
    input_variables=["urls"]
)


summary_prompt = PromptTemplate(
    template="""
Summarize each document separately.

Rules:
- Bullet points
- Keep facts
- No merging

Return list:
["summary1","summary2"]

Documents:
{documents}
""",
    input_variables=["documents"]
)


report_prompt = PromptTemplate(
    template="""
Write a professional research report from summaries.

Structure:
Title
Executive Summary
Key Findings
Comparative Insights
Important Facts
Conclusion

Summaries:
{summaries}
""",
    input_variables=["summaries"]
)

# =========================
# CHAIN
# =========================
chain = (
    extract_prompt
    | llm
    | parser
    | summary_prompt
    | llm
    | parser
    | report_prompt
    | llm
    | parser
)


# =========================
# LOGIC FUNCTION
# =========================
def generate_report(query):

    search_result = search_tool.invoke(query)

    urls = urls = [search_result["results"][item]["url"] for item in range(0,5)]

    output = chain.invoke({"urls": urls})

    return output, urls


# =========================
# UI INPUT
# =========================
user_query = st.text_area(
    "Enter Research Question",
    placeholder="Example: How can RAG reduce hallucinations?"
)

# =========================
# BUTTON
# =========================
if st.button("Generate Report"):

    if not user_query.strip():
        st.error("Please enter a question")
        st.stop()

    with st.spinner("Researching + Generating Report..."):

        try:
            report, urls = generate_report(user_query)

            st.success("Report Generated!")

            st.subheader("🔗 Sources")
            for u in urls:
                st.write(u)

            st.divider()

            st.subheader("📄 Final Report")
            st.markdown(report)

        except Exception as e:

            st.error(f"Error: {str(e)}")
