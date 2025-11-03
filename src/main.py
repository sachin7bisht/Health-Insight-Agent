import streamlit as st
from ui.home_page import render_home_page
from dotenv import load_dotenv

load_dotenv()
# Load environment variables
def main():
    st.set_page_config(page_title="HIA - Health Insights Agent", layout="centered")
    render_home_page()

if __name__ == "__main__":
    main()
