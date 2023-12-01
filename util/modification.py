import re

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

def codeModification(code, do_what):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0,
    )
    system_template = f"""You are a code generator. Your task is to give me a Python function to optimize the {do_what} complexity of the following code, along with the same test case, without any explanations,without any formatting or language specification, just the pure code and test case . The code is: {code}"""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = f"""Please give me a Python code function to optimize the {do_what} complexity of the following code, along with the same test case, without any explanations, without any formatting or language specification, just the pure code and test case. The code is: {code}"""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(code = code, do_what = do_what)
    return result # returns string

