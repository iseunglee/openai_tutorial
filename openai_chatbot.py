from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
openai_api_key=os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=openai_api_key)

MODEL = "gpt-3.5-turbo-1106"

want_to = """너는 아래 내용을 기반으로 너의 생각을 얘기 하는 로봇이야.
content
{}"""

content = ""

# GPT에게 질문하고 응답 받는 함수
def ask_to_gpt(messages):
    response = client.chat.completions.create(
        model=MODEL,
        top_p=0.1,
        temperature=0.1,
        messages=messages,
    )

    return response.choices[0].message.content

messages=[
        {'role': 'system', 'content': want_to.format(content)},
    ]

user_input = input('You: ')

messages.append(
    {'role': 'user', 'content': user_input},
)

response = ask_to_gpt(messages)

print(response)