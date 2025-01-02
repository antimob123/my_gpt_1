import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils import get_chat_response
import os

#openai_api_key = os.getenv("OPENAI_API_KEY")


st.title("MY_ChatGPT")
MyTokens = 100
with st.sidebar:
    openai_api_key = st.text_input("请输入密钥:", type='password')
    MyTokens = st.text_input("请输入Tokens值:", type='default')
    # st.markdown("[获取OpenAI API key](https://platform.openai.com/account/api-keys)")
    temperature_1 = st.slider("请选择温度值 (0.0 到 2.0)", 0.0, 2.0, 1.0)  # 默认值为1.0
    top_p_1 = st.slider("请选择 Top-p 值 (0.0 到 1.0)", 0.0, 1.0, 1.0)  # 默认值为 1.0
    # 输入 Frequency Penalty 值
    frequency_penalty_1 = st.slider("请选择 Frequency Penalty 值 (-2 到 2)", -2.0, 2.0, 0.0)  # 默认值为 0.0

# 确保 Tokens 是一个有效的整数并在合理范围内
if MyTokens:
    try:
        tokens_value = int(MyTokens)
        if not (0 <= tokens_value <= 500):
            st.error("Tokens值必须在 0 到 500 之间")
            tokens_value = None
    except ValueError:
        st.error("请输入有效的整数值作为 Tokens")
        tokens_value = None
else:
    tokens_value = None


if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "你好，有什么可以帮你的吗？"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not openai_api_key:
        st.info("请输入你的OpenAI API Key")
        # st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中，请稍等..."):
        response = get_chat_response(prompt, st.session_state["memory"],
                                     openai_api_key,tokens_value,temperature_1,top_p_1,frequency_penalty_1)
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)
