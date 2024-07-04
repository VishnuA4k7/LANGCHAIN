from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
import streamlit as st

from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "True"
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","Your a helpfull assistance. Please response to the user queries"),
        ("user","Vishnu Can answer your Questions:{question}")
    ]
)
st.title('LangChain demo with OLLAMA3 language')
input_text = st.text_input("search the topic you want")

llm = Ollama(model = "llama3")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({"question": input_text}))



