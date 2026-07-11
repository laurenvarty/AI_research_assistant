import streamlit as st

from src.pdf_loader import extract_text


st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚"
)


st.title("📚 AI Research Assistant")


uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)


if uploaded_file:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    text = extract_text(uploaded_file)

    st.subheader("Extracted text")

    st.text_area(
    "Extracted text",
    text,
    height=500
)
