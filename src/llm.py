# llm.py

from openai import OpenAI

from config import OPENAI_API_KEY


# Create OpenAI client and set up API key
client = OpenAI(
    api_key=OPENAI_API_KEY
)


def ask_llm(question, context):

    response = client.chat.completions.create(

        # Cheap model suitable for this project as many test runs to come
        model="gpt-4.1-mini",

        messages=[

            {
                "role": "system",
                "content":
                """
                You are an investment research assistant.
                Answer only using the provided context.
                """
            },

            {
                "role": "user",
                "content": f"""
                Context:
                {context}

                Question:
                {question}
                """
            }
        ]
    )


    return response.choices[0].message.content
    