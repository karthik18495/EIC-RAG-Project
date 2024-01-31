import os, sys
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["TRUBRICS_EMAIL"] = st.secrets["TRUBRICS_EMAIL"]
os.environ["TRUBRICS_PASSWORD"] = st.secrets["TRUBRICS_PASSWORD"]
os.environ["STREAMLIT_THEME_BASE"] = "dark"

if st.secrets.get("LANGCHAIN_API_KEY"):
    os.environ["LANGCHAIN_API_KEY"] = st.secrets["LANGCHAIN_API_KEY"]
    os.environ["LANGCHAIN_TRACING_V2"] = st.secrets["LANGCHAIN_TRACING_V2"]
    os.environ["LANGCHAIN_PROJECT"] = st.secrets["LANGCHAIN_PROJECT"]
    os.environ["LANGCHAIN_ENDPOINT"] = st.secrets["LANGCHAIN_ENDPOINT"]

st.set_page_config(
    page_title="AI4EIC-RAG QA-ChatBot",
    page_icon="https://indico.bnl.gov/event/19560/logo-410523303.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get help': 'https://eic.ai',
        'Report a bug': "https://github.com/wmdataphys/EIC-RAG-Project",
        'About': "# AI4EIC RAG System",
    }
)
st.warning("This project is being continuously developed. Please report any feedback to ai4eic@gmail.com")
col_l, col1, col2, col_r = st.columns([1, 3, 3, 1])

with col1:
    st.image("https://indico.bnl.gov/event/19560/logo-410523303.png")
with col2:
    st.title("""AI4EIC-RAG System""", anchor = "AI4EIC-RAG-QA-Bot", help = "Will Link to arxiv proceeding here.")

if st.session.get("user_name"):
    with st.sidebar():
        st.write("---")
        st.write("## Welcome back!")
        st.write("### " + st.session.get("first_name") + st.session.get("last_name"))
        st.write("---")


content = open("streamlit_app/Resources/Markdowns/introduction.md", "r").read()
st.markdown(content)
    
