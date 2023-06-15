import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY'] = apikey

st.image('./download.jpg')
st.subheader("ABHAY'S GPT")
st.subheader("Welcome to my project on AI&ML using langchain and pinecone vector database")

prompt = st.text_input('Tell me any topic or subject and Abhay will answer')

question = PromptTemplate(
    input_variables=  ['topic'],
    template= '''write a short and funny sentence/paragraph on {topic} as if it is written by Abhay Ranga, 
    who is a vegetarian, dank, dark-humour, witty, college student, basketball player and General Knowlege enthusiast in 10-20 words'''
)

llm=OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt= question, verbose=True)

if prompt:
    response = title_chain.run(topic = prompt)
    st.write(response)

 
