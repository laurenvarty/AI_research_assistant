# app.py

import streamlit as st

# Import the functions that make up our RAG pipeline
from src.pdf_loader import extract_pages
from src.chunking import chunk_pages
from src.embeddings import create_embeddings
from src.vector_store import create_vector_store
from src.retrieval import retrieve
from src.llm import ask_llm


# -----------------------------
# Streamlit page configuration
# -----------------------------

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚"
)


st.title("📚 AI Research Assistant")


# -----------------------------
# Upload PDF
# -----------------------------

uploaded_file = st.file_uploader(
    "Upload an investment document PDF",
    type=["pdf"]
)


# -----------------------------
# Process PDF
# -----------------------------
# This only runs once per uploaded PDF.
# session_state prevents rebuilding embeddings
# every time Streamlit reruns.

if uploaded_file and "index" not in st.session_state:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )


    # Extract text while keeping page numbers
    pages = extract_pages(uploaded_file)


    # Split pages into smaller chunks
    chunks = chunk_pages(pages)


    # Convert chunks into embeddings/vectors
    embeddings = create_embeddings(chunks)


    # Store vectors in FAISS
    index = create_vector_store(embeddings)


    # Save objects for reuse
    st.session_state.pages = pages
    st.session_state.chunks = chunks
    st.session_state.index = index



# -----------------------------
# Question answering
# -----------------------------

if "index" in st.session_state:


    question = st.text_input(
        "Ask a question about the document"
    )


    if question:


        # Find the most relevant chunks
        results = retrieve(
            question,
            st.session_state.index,
            st.session_state.chunks
        )


        # Extract only the text from chunks
        # Page numbers stay attached for references
        context = "\n\n".join(
            [
                result["text"]
                for result in results
            ]
        )


        # Send context + question to OpenAI
        answer = ask_llm(
            question,
            context
        )


        st.subheader("Answer")

        st.write(answer)



        # -------------------------
        # Show document references
        # -------------------------

        st.subheader("References")


        # Remove duplicate page numbers
        pages = sorted(
            set(
                [
                    result["page"]
                    for result in results
                ]
            )
        )


        for page in pages:

            st.write(
                f"📄 Page {page}"
            )



    # -----------------------------
    # Show extracted text
    # -----------------------------
    # This is outside the question block,
    # so it appears even before asking questions.

    st.subheader("Extracted Text")


    # Combine pages back into readable text
    display_text = "\n\n".join(
        [
            f"--- Page {page['page']} ---\n{page['text']}"
            for page in st.session_state.pages
        ]
    )


    st.text_area(
        "Extracted Text",
        display_text,
        height=500
    )
    