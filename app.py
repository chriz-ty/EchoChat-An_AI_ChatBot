#Q&A Chatbot

from langchain_community.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
os.environ["OPEN_API_KEY"]="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"
def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),model_name="gpt-3.5-turbo-instruct", temperature=0.5)
    response=llm(question)
    return response

#initilaize streamlit app

st.set_page_config(page_title="Echo Chat")
st.header("Echo Chat - An AI ChatBot")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

if submit:
    st.subheader("The response is: ")
    st.write(response)