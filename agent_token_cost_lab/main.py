from dotenv import load_dotenv 
import os 
from openai import OpenAI 
 
load_dotenv() 
 
client = OpenAI( 
    api_key=os.getenv("DEEPSEEK_API_KEY"), 
    base_url=os.getenv("DEEPSEEK_BASE_URL") 
) 
 
response = client.chat.completions.create( 
    model=os.getenv("DEEPSEEK_MODEL"), 
    messages=[ 
        {"role": "user", "content": "你好，介绍一下自己"} 
    ], 
    temperature=0.7, 
    max_tokens=512 
) 
 
print("DeepSeek 回复：") 
print(response.choices[0].message.content) 
