import google.generativeai as genai
genai.configure(api_key="AIzaSyDGBlv5zGjsK-3VXPGRmUQezsnJsC7h2JY")
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat()
while True:
    message = input("You: ")
    response = chat.send_message(message)
    print("Gemini: " + response.text)