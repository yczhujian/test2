import streamlit as st
from streamlit_chat import message


def main():
    st.set_page_config(
        page_title='Crown & Rights ChatGPT',
        page_icon=':books:'
    )
    st.header('冠和权专属chatGPT :books:')

    message("您好！欢迎来到冠和权的chatGPT")
    message("谢谢！", is_user=True)  # align's the message to the right

    with st.sidebar:
        usrer_input = st.text_input("您的消息:", key="user_input")


if __name__ == '__main__':
    main()