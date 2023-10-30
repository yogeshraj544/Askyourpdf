from config import openai_api_key
import streamlit as st
import openai
openai.api_key = openai_api_key

def main():
    

    st.set_page_config(page_title="Ask your pdf")
    st.header("Ask your pdf ")
    pdf = st.file_uploader("Upload your pdf", type="pdf")