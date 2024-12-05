from plugins.chatcompletion_plugin import ChatCompletionPlugin

def main():
    # Initialize the ChatCompletionPlugin
    chat_plugin = ChatCompletionPlugin()

    print("Welcome to the Semantic Kernel Chatbot!")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        else:
            response = chat_plugin.get_response(user_input)
            print(f"\nBot: {response}")

if __name__ == "__main__":
    main()
