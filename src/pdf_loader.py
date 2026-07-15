# pdf_loader.py

import fitz  # PyMuPDF


def extract_pages(uploaded_file):

    # Open the uploaded PDF
    document = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )


    pages = []


    # Go through each page extracting text and saving page number
    for page_number, page in enumerate(document):

        
        text = page.get_text()


        
        pages.append(
            {
                "text": text,
                "page": page_number + 1
            }
        )


    return pages
    