from openai import OpenAI

# Create a client with your API key
client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

def chat_with_gpt(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("App started...")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        reply = chat_with_gpt(user_input)
        print("GPT:", reply)