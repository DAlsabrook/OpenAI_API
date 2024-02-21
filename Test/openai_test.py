import os
from openai import OpenAI

def chat_gpt(mood, how_detailed, message):
    if message == "":
        print("You must fill in a message to the chat!")
        return 0
    client = OpenAI(
        api_key= os.getenv('OPENAI_API_KEY')
    )

    complete = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""Response mood should be: {mood}.
                Level of detail in response: {how_detailed} detailed.
                Promt: {message}""",
            }
        ],
        model="gpt-3.5-turbo",
    )
    response = complete.choices[0].message.content
    print(complete)
    print(f"\nChatGPT:\n{response}\n")


#The mood you want the response sent back in
mood = "Kind"

#Detailed suggestions not very, moderate, very, extremely
how_detailed = "moderate"

#Message you want to send to GPT
message = "What day of the week will it be in exactly 1248762515627382 days"


if __name__ == "__main__":
    chat_gpt(mood, how_detailed, message)
