from transformers import pipeline

# Load pretrained model (GPT-2)
chatbot = pipeline("text-generation", model="gpt2")

def start_chat():
    print("🤖 PyBot AI: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("🤖 PyBot AI: Goodbye! Have a nice day.")
            break
        response = chatbot(user_input, max_length=50, num_return_sequences=1, truncation=True)
        reply = response[0]["generated_text"].replace(user_input, "").strip()
        print("🤖 PyBot AI:", reply)

if __name__ == "__main__":
    start_chat()
