# AI Research Assistant

This project uses Retrieval Augmented Generation (RAG) to allow a user to query documents. The initial intention for it was for scientific papers to be summarised and made searchable for efficiency in my studies but could be applied to any PDF information document.

## Features

-uploads PDFs

-extracts documents of text

-chunks documents for retrieval of information

-embeddings

-stores vectors using FAISS

-asks the user their question using OpenAI GPT

-provides page references for checking of answers

## Structure of Project

PDF

↓

Text extraction

↓

Chunking

↓

Embeddings

↓

FAISS vector search

↓

LLM response

## Installation and setup

-To use this copy and paste the code below into the terminal 

-pip install -r requirements.txt

-Add your API key:

-Create `.env`

-OPENAI_API_KEY=your_key_here

## Running the app

-streamlit run app.py

## Potential Future Improvements and ideas

-may be used for querying multiple different documents

-can be integrated with email workflows to extract important messages

-can be used for investment information or company information

-could be used for monitoring trends or important global news

-This is my first ever uploaded project so I'll continue to iterate on it as I develop -my AI engineering more.



# AI_research_assistant
