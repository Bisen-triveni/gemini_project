import google.generativeai as genai
genai.configure(api_key= "AIzaSyDGBlv5zGjsK-3VXPGRmUQezsnJsC7h2JY")
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("What is the meaning of life?")
print(response.text)