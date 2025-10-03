import random

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello! How can I help you?", "Hey!"],
    "how are you": ["I'm just a bot, but I'm doing great!", "I'm fine, thanks!", "All good!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "your name": ["I'm a Python Chatbot 🤖", "You can call me PyBot."]
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry, I didn't understand that."

def chatbot():
    print("🤖 PyBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("🤖 PyBot: Goodbye! Have a nice day.")
            break
        print("🤖 PyBot:", get_response(user_input))

if __name__ == "__main__":
    chatbot()
