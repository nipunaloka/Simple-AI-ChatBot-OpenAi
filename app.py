from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.environ["OPEN_API_KEY"]

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

while True:

    question = input("User: ")

    if question != "exit":

        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            max_tokens=50,  
            n=1,
            temperature=0.3,
            messages=[ 
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        # max_tokens: The maximum number of tokens to generate in the response. The total length of input and output tokens should not exceed the model's context length.
        # n: The number of response choices to generate. If you want multiple responses, set this to a value greater than 1.
        # temperature: Controls the randomness of the output. Higher values (e.g., 0.7) make the output more random, while lower values (e.g., 0.2) make it more focused and deterministic.

        for choice in response.choices:
            print(f"AI: {choice.message.content}")
    
    else:
        print("AI: Exiting the chat.")
        break
