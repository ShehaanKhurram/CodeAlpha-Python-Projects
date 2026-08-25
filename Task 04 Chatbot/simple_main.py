def get_response(user_input):
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi there! How can I help you today?"

    elif text in ("how are you", "how are you?"):
        return "I'm fine, thanks! How about you?"

    elif "your name" in text:
        return "I'm a simple chatbot built for a practice purpose."

    elif "help" in text:
        return "You can say hello, ask how I am, or say bye to exit."

    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I didn't understand that. Try saying 'hello' or 'help'."

def chat():
    print("=" * 40)
    print("   SIMPLE RULE-BASED CHATBOT")
    print("=" * 40)
    print("Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        if not user_input.strip():
            print("Bot: Please type something.")
            continue

        response = get_response(user_input)
        print(f"Bot: {response}")

        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break

if __name__ == "__main__":
    chat()