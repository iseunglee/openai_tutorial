from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4-vision-preview"
client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
  model=MODEL,
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "이 이미지는 무슨 내용이니?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])
