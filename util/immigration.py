import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.document_loaders import *
from langchain.chains.summarize import load_summarize_chain
import tempfile
from langchain.docstore.document import Document

def codeImmigration(code, lan):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0,
    )
    system_template = f"""You are a code generator. Your task is to provide me with a complete {lan} code snippet that has the same functionality as the following Python code, including all necessary headers and namespaces. Also, include the same test case. No explanations or formatting are needed, just the pure code and test case. The Python code is: {code}."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = f"""Please provide me with a complete {lan} code snippet that has the same functionality as the following Python code, including all necessary headers and namespaces. Also, include the same test case. No explanations or formatting are needed, just the pure code and test case. The Python code is: {code}."""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(code = code, lan = lan)
    return result # returns string
