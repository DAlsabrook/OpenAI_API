import os
from openai import OpenAI


client = OpenAI(
    # This is the default and can be omitted
    #api_key="",
    api_key= os.getenv('OPENAI_API_KEY')
)

complete = client.chat.completions.create(
    messages=[
        {
            "role": "user", "content": "create an image of a dog",
        }
    ],
    model="gpt-3.5-turbo",
)
response = complete.choices[0].message.content
print(response)
