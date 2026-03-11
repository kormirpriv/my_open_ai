from my_open_ai.chat_service import ChatService

chat = ChatService()

while True:
    user_input = input("👤 You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("See you later!")
        break

    response = chat.ask(user_input)

    print(f"🤖 Bot: {response}")