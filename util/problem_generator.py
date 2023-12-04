import streamlit as st
import re
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.document_loaders import *
from langchain.chains.summarize import load_summarize_chain
import tempfile
from langchain.docstore.document import Document

def codeGenerator(times, difficulty, do_what):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0,
    )
    system_template = f"""You are a code generator. This is the {times} time I asked you. Your task is to give me a python function for a different ever {difficulty} difficulty problem from LeetCode that is not {do_what}-optimal, along with a test case, without any explanations, formatting or language specification. Just the pure code and test case."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = f"""This is the {times} time I asked you. Please give me a python function for a different ever {difficulty} difficulty problem from LeetCode that is not {do_what}-optimal, along with a test case, without any explanations, formatting or language specification. Just the pure code and test case."""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(times = times, difficulty = difficulty, do_what = do_what)
    return result # returns string

