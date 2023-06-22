import os
import json
import numpy
import openai
import streamlit as st
from dotenv import load_dotenv
from fuzzywuzzy import fuzz

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

    keyword_scores = []
    vector_scores = []
    for chunk in index:

        # Gives result of 0 - 100
        keyword_score = fuzz.partial_token_set_ratio(
            question, chunk["keywords"])
        # Gives result of 0 - 1
        vector_score = similarity(question_embedding, chunk["embedding"]) * 100

        total_score = vector_score + keyword_score

        vector_scores.append(
            {"content": chunk["content"], "score": total_score, "source": chunk["source"]})

    sorted_scores = sorted(
        vector_scores, key=lambda d: d["score"], reverse=True)

    log(sorted_scores, 'data/chat_output', 'scores')

    contexts = [s["content"] for s in sorted_scores[0:3]]
    formatted_context = "\n\n---\n\n".join(contexts)

    prompt = '''Answer the following question given the provided context. Think carefully and pay attention to each given situation. Reason through the logic of the rules before giving as accurate an answer as possible. Include all relevant information.
    Context: <<CONTEXT>>
    \n\n=== end of context ===\n\n
    Question: <<QUESTION>>
    '''
    prompt_prepped = prompt.replace(
        '<<QUESTION>>', question).replace('<<CONTEXT>>', formatted_context)

    chat_response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": "You are an expert on the board game 'Nemesis', and your job is to provide answers and information on the rules of the game using excerpts from the rulebook which will be provided for you."},
        {"role": "user", "content": prompt_prepped},
    ])
    answer = chat_response['choices'][0]['message']['content']

    log_data = {
        "userMessage": prompt_prepped,
        "assistantMessage": answer
    }
    log(log_data, 'data/chat_output', 'question-answer')

    st.write(answer)

    for context in sorted_scores[0:3]:
        st.write(f'Source:\n\n{context["source"]}')
        st.write(f'\n\n{context["content"]}')
        st.write('\n\n\n\n')
