# chunking.py

from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_pages(pages):

    # Splits the text into chunks of 800 characters with 150 characters of overlap for context
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )


    chunks = []


    # Loop through every PDF page
    for page in pages:

        page_chunks = splitter.split_text(
            page["text"]
        )


        # Save each chunk together with its source page
        for chunk in page_chunks:

            chunks.append(
                {
                    "text": chunk,
                    "page": page["page"]
                }
            )


    return chunks
    