import os
import tiktoken
from langchain.text_splitter import RecursiveCharacterTextSplitter
from datetime import datetime
from fastapi.encoders import jsonable_encoder
import json
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


INPUT_DIR = "data/indexer_input"
OUTPUT_DIR = "data/indexer_output"

TOKENIZER = "cl100k_base"
CHAT_MODEL = "gpt-3.5-turbo"
EMBEDDING_MODEL = "text-embedding-ada-002"

CHUNK_SIZE = 500
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

    timestamp_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    with open(f"{OUTPUT_DIR}/{timestamp_str}_chunks.json", "w") as file:
        file.write(json.dumps(jsonable_encoder(chunks)))
