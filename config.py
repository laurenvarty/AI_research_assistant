import os

from dotenv import load_dotenv


# Loads variables from the .env file
load_dotenv()


# Gets your API key safely
# instead of writing it directly in code
OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)
