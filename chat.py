import os
import json
import numpy
import openai
import streamlit as st
from dotenv import load_dotenv

from utils import log

load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']


def similarity(v1, v2):
    return numpy.dot(v1, v2)


st.set_page_config(
    page_title="Streamlit Search - Demo",
    page_icon=":robot:"
)

st.title("Nemesis chatbot")
st.subheader("Ask questions about Nemesis rules")

question = st.text_input("Enter your question here", "", key="input")

if st.button('Submit', key='generationSubmit'):
    # get relevant contexts
    question_embedding_response = openai.Embedding.create(
        input=question, engine="text-embedding-ada-002")
    question_embedding = question_embedding_response["data"][0]["embedding"]

    with open('index.json', 'r') as file:
        index = json.load(file)

    scores = []
    for chunk in index:
        score = similarity(question_embedding, chunk["embedding"])
        scores.append(
            {"content": chunk["content"], "score": score, "source": chunk["source"]})

    sorted_scores = sorted(scores, key=lambda d: d["score"], reverse=True)

    log(sorted_scores, 'data/chat_output', 'scores')

    contexts = sorted_scores[0]

    # Build a prompt to provide the original query, the result and ask to summarise for the user
    summary_prompt = '''Summarise this result to answer the search query a user has sent.
    Search query: SEARCH_QUERY_HERE
    Search result: SEARCH_RESULT_HERE
    Summary:
    '''
    summary_prepped = summary_prompt.replace(
        'SEARCH_QUERY_HERE', question).replace('SEARCH_RESULT_HERE', contexts["content"])

    chat_response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": "You are an expert on the rules of board games."},
        {"role": "user", "content": summary_prepped},
    ])

    log(chat_response, 'data/chat_output', 'chat-response')

    answer = chat_response['choices'][0]['message']['content']

    st.write(answer)

    st.write(contexts["source"])
    st.write(contexts["content"])
