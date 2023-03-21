import streamlit as st
import openai


"""
# Welcome to Streamlit!
Jean Code to open a Chat GPT Prompt
"""


openai.api_key = "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"

def ask_chatgpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text
    return message.strip()


def app():
    st.title("ChatGPT")
    user_input = st.text_input("You: ")
    if user_input:
        response = ask_chatgpt(user_input)
        st.text_area("ChatGPT:", value=response, height=200)
