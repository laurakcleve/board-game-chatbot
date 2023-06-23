import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

EMBEDDING_MODEL = "text-embedding-ada-002"


def get_embedding(text):
    embedding_response = openai.Embedding.create(input=text, engine=EMBEDDING_MODEL)
    return embedding_response["data"][0]["embedding"]
