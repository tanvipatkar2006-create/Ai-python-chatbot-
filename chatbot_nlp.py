import random
from nltk.chat.util import Chat, reflections

# Patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi!"]],
    [r"how are you ?", ["I'm doing well, thank you!", "I'm great, and you?"]],
    [r"what is your name ?", ["I'm PyBot, your chatbot.", "You can call me PyBot 🤖"]],
    [r"(.*) your hobby ?", ["I like chatting with humans!", "Learning new things is my hobby."]],
    [r"(.*) created you ?", ["I was created by a Python developer!"]],
    [r"quit", ["Goodbye! Take care.", "See you soon!"]],
]

# Create chatbot
chatbot = Chat(pairs, reflections)

def start_chat():
    print("🤖 PyBot: Hello! Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()
