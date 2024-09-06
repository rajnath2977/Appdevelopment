#pip install streamlit
#!pip install -qU langchain langchain-openai langchain-google-genai
import os
import langchain-oprnai
import streamlit as st

os.environ["OPENAI_API_KEY"] = "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"

st.title("Tweet Generator - V 🐦")

st.subheader("🚀 Generate tweets on any topic")

topic = st.text_input("Topic")
number = st.number_input("Number of tweets", min_value = 1, max_value = 10, value = 1, step = 1)


# Import ChatOpenAI module
from langchain_openai import ChatOpenAI

# Initialize OpenAI's GPT 3.5 model
gpt3_model = ChatOpenAI(model_name = "gpt-3.5-turbo-0125")


if st.button("Generate"):
    prompt = f"Give me {number} tweets on {topic}."
    response = gpt3_model.invoke(prompt)
    st.write(response.content)


# python test.py
