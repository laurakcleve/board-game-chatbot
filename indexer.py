import os
import tiktoken
from langchain.text_splitter import RecursiveCharacterTextSplitter
from fastapi.encoders import jsonable_encoder
import json
from dotenv import load_dotenv
import openai

from utils import get_timestamp_str

load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']


INPUT_DIR = "data/indexer_input"
OUTPUT_DIR = "data/indexer_output"

TOKENIZER = "cl100k_base"
CHAT_MODEL = "gpt-3.5-turbo"
EMBEDDING_MODEL = "text-embedding-ada-002"

CHUNK_SIZE = 1100
CHUNK_OVERLAP = 50


if __name__ == "__main__":

    encoding = tiktoken.get_encoding(TOKENIZER)

    files = ([x for x in os.listdir(
        os.path.join(os.curdir, INPUT_DIR))])

    texts = []
    sources = []

    for file in files:
        # file = faq.txt, rulebook.txt, etc.

        file_path = os.path.join(INPUT_DIR, file)
        # file_path = data/indexer_input/faq.txt, etc.

        source = file.replace(".txt", "")
        sources.append({"source": source})

        with open(file_path, 'r') as f:
            texts.append(f.read())

    def tiktoken_len(text):
        tokens = encoding.encode(text, disallowed_special=())
        return len(tokens)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP, length_function=tiktoken_len
    )

    chunks = text_splitter.create_documents(texts, metadatas=sources)

    with open(f"{OUTPUT_DIR}/{get_timestamp_str()}_chunks.json", "w") as file:
        file.write(json.dumps(jsonable_encoder(chunks)))

    index = []

    for chunk in chunks:
        response = openai.Embedding.create(
            input=chunk.page_content, engine=EMBEDDING_MODEL)
        embedding = response["data"][0]["embedding"]

        index.append({"content": chunk.page_content,
                     "source": chunk.metadata["source"], "embedding": embedding})

    with open(f"{OUTPUT_DIR}/{get_timestamp_str()}_index.json", "w") as file:
        file.write(json.dumps(index))
