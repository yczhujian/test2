import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

# 初始化
def init():
    load_dotenv()
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    st.set_page_config(
        page_title='Crown & Rights ChatGPT',
        page_icon=':books:'
    )


def main():
    init()

    chat = ChatOpenAI(temperature=0)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="冠和权AI机器人助力您的研发工作.")
        ]

    st.header('冠和权专属chatGPT :books:')

    with st.sidebar:
        user_input = st.text_input("您的消息:", key="user_input")

    if user_input:
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("冠和权AI正在思考"):
            response = chat(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))

    messages = st.session_state.get("messages", [])
    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=str(i) + '_user')
        else:
            message(msg.content,is_user=False, key=str(i) + '_ai')

if __name__ == '__main__':
    main()