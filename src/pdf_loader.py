import fitz  # PyMuPDF


def extract_pages(uploaded_file):

    # Open the uploaded PDF
    document = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )


    pages = []


    # Go through each page
    for page_number, page in enumerate(document):

        # Extract text from this page
        text = page.get_text()


        # Save text + page number
        pages.append(
            {
                "text": text,
                "page": page_number + 1
            }
        )


    return pages
    