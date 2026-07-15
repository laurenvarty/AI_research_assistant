# summariser.py

from llm import ask_llm

# Summarises the text, could be used to summarise the entire PDF or just the retrieved chunks
# Possible adaptation for investment memo summarisation
def summarise(text):

    prompt = f"""
Summarise this investment memo into:

- Company
- Industry
- Business model
- Revenue
- Risks
- Opportunities
- Investment thesis

{text}
"""

    return ask_llm(prompt, "")

    if st.button("Generate Summary"):

    summary = summarise(text)

    st.write(summary)
    