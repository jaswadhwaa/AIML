import openai
import os

# Set your OpenAI API key
openai.api_key = "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"
# Alternatively, you can set it as an environment variable and retrieve it like this:
# openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize conversation history
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def chat_with_gpt(user_input):
    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Get the response from the API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )

    # Get the assistant's message
    assistant_message = response['choices'][0]['message']['content']

    # Add the assistant's response to the conversation history
    conversation_history.append({"role": "assistant", "content": assistant_message})

    return assistant_message

print("Chatbot is ready to talk! Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    bot_response = chat_with_gpt(user_input)
    print("ChatGPT:", bot_response)