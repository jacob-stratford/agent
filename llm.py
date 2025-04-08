# File for the LLm

#print('hello world')

from google import genai

with open("../API_KEY.txt", "r") as file:
    api_key = file.read().strip()
# Initialize the Google GenAI client with your API key 

print(api_key)
#quit()

client = genai.Client(api_key=api_key)
client.set_system_prompt("You are an AI assistant. Always provide concise and to-the-point responses, as token usage is limited.")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="What is the capital of France?"
)

print(response.text)