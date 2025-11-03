import streamlit as st
from utils.pdf_extractor import extract_text_from_pdf
from service.openai_service import analyse_health_report
from service.supabase_service import save_report_to_db


def render_home_page():
    """Renders the main Streamlit home page for the HIA app."""
    
    st.title("🩺 HIA — Health Insights Agent")
    st.markdown("Upload your **blood report (PDF)** to get AI-based analysis and insights.")

    # File uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file:
        st.info(f"📄 Uploaded: **{uploaded_file.name}**")
        
        with st.spinner("🔍 Extracting text from PDF..."):
            extracted_text = extract_text_from_pdf(uploaded_file)

        # If extraction fails, extracted_text will contain error string
        if extracted_text.startswith("Error") or "Invalid" in extracted_text or "exceeds" in extracted_text:
            st.error(extracted_text)
            return

        st.success("✅ Text extracted successfully!")
        with st.expander("Show Extracted Text"):
            st.text(extracted_text)

        if st.button("🤖 Analyze Report"):
            with st.spinner("Analyzing report with AI..."):
                result = analyse_health_report(extracted_text)

            if result.startswith("Error"):
                st.error(result)
            else:
                st.subheader("🧠 AI Analysis Result:")
                st.write(result)

                # Save to Supabase
                save_response = save_report_to_db(uploaded_file.name, extracted_text, result)
                if isinstance(save_response, str) and "Error" in save_response:
                    st.warning(save_response)
                else:
                    st.success("✅ Report saved to database!")