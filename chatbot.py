def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm ChatBuddy, your simple chatbot friend!"
    elif "weather" in user_input:
        return "I can't check the weather right now, but I hope it's nice where you are!"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure about that. Can you ask something else?"

print(" ChatBuddy: Hello! Type 'bye' to exit.")
while True:
    user = input("You: ")
    reply = chatbot_response(user)
    print("ChatBuddy:", reply)
    if "bye" in user.lower() or "exit" in user.lower():
        break
