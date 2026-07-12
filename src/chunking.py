from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_pages(pages):

    # Split documents into smaller pieces
    # so the embedding model can search them effectively
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )


    chunks = []


    # Loop through every PDF page
    for page in pages:

        # Split this page's text into chunks
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
    