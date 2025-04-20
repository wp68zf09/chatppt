import gradio as gr
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from llm import llm


llm=llm()
# 读取 formatter.txt 作为 systemPrompt
def read_system_prompt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# 使用 deepseek 大模型将用户输入转换为 Markdown
def convert_to_markdown(user_input, system_prompt, chat_model):
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]
    response = chat_model(messages)
    return response.content

# 保存 Markdown 内容到文件
def save_markdown(content, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


# 创建 Gradio 界面
iface = gr.Interface(
    fn=llm.convert_and_save_markdown,
    inputs=gr.Textbox(lines=10, placeholder="请输入要转换为 Markdown 的内容..."),
    outputs=gr.File(label="下载生成的 Markdown 文件"),
    title="Markdown 转换工具",
    description="输入内容后，点击按钮将内容转换为 Markdown 文件并下载。"
)

# 启动 Gradio 界面
if __name__ == "__main__":
    iface.launch(share=True, server_name="0.0.0.0")  # 启动界面并设置为公共可访问