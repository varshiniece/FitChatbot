import openai
import streamlit as st
from streamlit_chat import message
openai.api_key = st.secrets['pass']
def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message 
#Creating the chatbot interface
st.title("chatBot : Streamlit + openAI")

