def chatbot():
    print("Hello!, I am your chatbot and I am here to listen to you. Share whatever is on your mind, and I will do my best to understand and respond to you.")
    while(True):
        user_input = input("You: ")
        print(f"Chatbot: You said: {user_input}")
        if "exit" in user_input.lower():
            print("Chatbot: Goodbye! Take care.")
            break


chatbot()
