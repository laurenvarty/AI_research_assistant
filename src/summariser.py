from llm import ask_llm


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
    