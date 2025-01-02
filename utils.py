from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

import os
from langchain.memory import ConversationBufferMemory
from openai import OpenAI



# def get_chat_response(prompt, memory, openai_api_key,tokens,my_temperature):
#     model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key,base_url="https://api.aigc369.com/v1")
#     chain = ConversationChain(llm=model, memory=memory)
#
#     response = chain.invoke({"input": prompt})
#     max_tokens = tokens  # 将 tokens 参数传递给 max_tokens
#     temperature = my_temperature
#     return response["response"]

def get_chat_response(prompt, memory, openai_api_key, tokens, my_temperature, top_p, frequency_penalty):
    # 将参数传递给模型初始化
    model = ChatOpenAI(
        model="gpt-3.5-turbo",        # 使用 GPT-3.5-turbo 模型
        openai_api_key=openai_api_key,
        base_url="https://api.aigc369.com/v1",  # API 基础 URL
        max_tokens=tokens,            # 设置最大 token 数量
        temperature=my_temperature,   # 设置温度值
        top_p=top_p,                  # 设置 Top-p 值
        frequency_penalty=frequency_penalty  # 设置 Frequency Penalty 值
    )

    # 创建对话链
    chain = ConversationChain(llm=model, memory=memory)

    # 调用对话链并获取响应
    response = chain.invoke({"input": prompt})

    return response["response"]

# memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("牛顿提出过哪些知名的定律？", memory, os.getenv("OPENAI_API_KEY")))
# print(get_chat_response("我上一个问题是什么？", memory, os.getenv("OPENAI_API_KEY")))

