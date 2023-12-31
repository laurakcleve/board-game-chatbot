import os
import json
import tiktoken
from langchain.text_splitter import RecursiveCharacterTextSplitter
from fastapi.encoders import jsonable_encoder
from dotenv import load_dotenv
import openai
from utils.openai_helpers import get_embedding

from utils.utils import get_timestamp_str

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]


INPUT_DIR = "data/indexer_input"
OUTPUT_DIR = "data/indexer_output"

TOKENIZER = "cl100k_base"
EMBEDDING_MODEL = "text-embedding-ada-002"
CHAT_MODEL = "gpt-4"

CHUNK_SIZE = 100
CHUNK_OVERLAP = 0


if __name__ == "__main__":
    encoding = tiktoken.get_encoding(TOKENIZER)

    files = [x for x in os.listdir(os.path.join(os.curdir, INPUT_DIR))]

    texts = []
    sources = []

    for file in files:
        # file = faq.txt, rulebook.txt, etc.

        file_path = os.path.join(INPUT_DIR, file)
        # file_path = data/indexer_input/faq.txt, etc.

        source = file.replace(".txt", "")
        sources.append({"source": source})

        with open(file_path, "r") as f:
            texts.append(f.read())

    def tiktoken_len(text):
        tokens = encoding.encode(text, disallowed_special=())
        return len(tokens)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=tiktoken_len,
        separators=["\n\n", "\n", r"\.\s"],
    )

    chunks = text_splitter.create_documents(texts, metadatas=sources)

    with open(f"{OUTPUT_DIR}/{get_timestamp_str()}_chunks.json", "w") as file:
        file.write(json.dumps(jsonable_encoder(chunks)))

    index = []

    for chunk in chunks:
        try:
            embedding = get_embedding(chunk.page_content)

            # keywords_response = openai.ChatCompletion.create(model=CHAT_MODEL, messages=[
            #     {"role": "user", "content": f"Extract keywords from the following text. Format them as an array of strings.\n\n{chunk.page_content}"}
            # ])
            # keywords = json.loads(
            #     keywords_response["choices"][0]["message"]["content"])

            # index.append({"content": chunk.page_content,
            #               "source": chunk.metadata["source"], "embedding": embedding, "keywords": keywords})
            index.append(
                {
                    "content": chunk.page_content,
                    "source": chunk.metadata["source"],
                    "embedding": embedding,
                }
            )

        except Exception as e:
            print(f"Error occurred: {e}")
            break

    with open(f"{OUTPUT_DIR}/{get_timestamp_str()}_index.json", "w") as file:
        file.write(json.dumps(index))
