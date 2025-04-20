import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
class llm:
    # 读取 formatter.txt 作为 systemPrompt
    def read_system_prompt(self,file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    # 使用 deepseek 大模型将用户输入转换为 Markdown
    def convert_to_markdown(self,user_input, system_prompt, chat_model):
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_input)
        ]
        response = chat_model(messages)
        return response.content

    # 保存 Markdown 内容到文件
    def save_markdown(self,content, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    # 主方法，转换用户输入为 Markdown 并保存到文件
    def convert_and_save_markdown(self,user_input):
        # 配置 deepseek 大模型
        chat_model = ChatOpenAI(
            model="deepseek-chat",
            base_url="https://api.deepseek.com",
            api_key="sk-3e5ff44e82b745a7ab7a748b806951c2",
            temperature=0.5,
            max_tokens=4000
        )

        # 读取 systemPrompt
        system_prompt = self.read_system_prompt('./prompts/formatter.txt')

        # 转换为 Markdown
        markdown_content = self.convert_to_markdown(user_input, system_prompt, chat_model)

        # 定义输出文件路径
        output_file_path = os.path.join('inputs', 'user_input.md')

        # 保存 Markdown 文件
        self.save_markdown(markdown_content, output_file_path)

        return output_file_path

# # 示例调用
# if __name__ == "__main__":
#     # 获取用户输入
#     user_input = input("请输入要转换为 Markdown 的内容: ")

#     # 定义输出文件路径
#     output_file_path = os.path.join('inputs', 'user_input.md')

#     # 调用 convert_and_save_markdown 方法
#     convert_and_save_markdown(user_input, output_file_path)