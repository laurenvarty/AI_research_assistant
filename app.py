#app.py

# Importing functions and libraries from the src and streamlit to create a front end interface 

import streamlit as st
from src.pdf_loader import extract_pages
from src.chunking import chunk_pages
from src.embeddings import create_embeddings
from src.vector_store import create_vector_store
from src.retrieval import retrieve
from src.llm import ask_llm



# Streamlit Page Configuration
# Configuring the page first before displaying any content on the interface

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Reduce the default spacing around the page to make it more visually apealing

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)



# Sidebar
# Display instructions for using the application.

with st.sidebar:
    st.title("📑 AI Research Assistant")

    st.markdown("""
    ### How to use
    1. Upload a PDF
    2. Wait for processing
    3. Ask questions
    4. View references
    """)



# Main Page

st.title("📑 AI Research Assistant")
st.caption("Upload an investment document and ask questions using AI.")



# Upload PDF
# The uploaded file is stored in memory and passed into the RAG pipeline for processing.

with st.container(border=True):
    uploaded_file = st.file_uploader(
        "Upload an investment document PDF",
        type=["pdf"]
    )



# Build the RAG Knowledge Base
# This block only runs once for each uploaded PDF.
# The processed data is stored in Streamlit's session_state so the document isn't rebuilt every
# time the page refreshes for efficiency.

if uploaded_file and "index" not in st.session_state:

    st.success(f"Uploaded: {uploaded_file.name}")

    # Extract text from every PDF page
    pages = extract_pages(uploaded_file)

    # Split large pages into smaller chunks for better retrieval.
    chunks = chunk_pages(pages)

    # Convert each text chunk into a vector embedding.    
    # Embeddings capture the semantic meaning of the text, allows similar content to be retrieved even when
    # different wording is used in the user's question.
    embeddings = create_embeddings(chunks)

    # Store the embeddings inside a FAISS vector database for fast search.

    # FAISS enables fast nearest-neighbour search, making
    # retrieval efficient even for large document collections.
    index = create_vector_store(embeddings)

    # Save everything so it can be reused without having to rebuild the index.
    st.session_state.pages = pages
    st.session_state.chunks = chunks
    st.session_state.index = index



# Question Answering
# Once a document has been indexed, the user can ask questions about its contents.

if "index" in st.session_state:

    # Display some information about the document and the number of chunks
    c1, c2 = st.columns(2)

    c1.metric("Pages", len(st.session_state.pages))
    c2.metric("Chunks", len(st.session_state.chunks))

    # Text box for the user's question.
    question = st.text_input(
        "Ask a question about the document"
    )


    if question:

        # Retrieve the most relevant chunks using similarity search.
        results = retrieve(
            question,
            st.session_state.index,
            st.session_state.chunks
        )

        # Combine the retrieved chunks into one string for the LLM and send the context and question.
        context = "\n\n".join(
            result["text"]
            for result in results
        )

        answer = ask_llm(
            question,
            context
        )

        # Display the generated answer.
        st.subheader("Answer")
        st.write(answer)


        # References
        # Show which pages the retrieved chunks came from.

        with st.expander("References"):

            reference_pages = sorted(
                set(
                    result["page"]
                    for result in results
                )
            )

            for page in reference_pages:
                st.write(f"📄 Page {page}")


    # Extracted Text
    # Display the raw extracted document text for transparency and debugging.

    with st.expander("Extracted Text"):

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

