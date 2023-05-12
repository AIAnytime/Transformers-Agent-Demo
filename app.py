import os
# import openai
from transformers.tools import OpenAiAgent
from dotenv import load_dotenv

load_dotenv()

# openai.api_key = os.getenv('OPENAI_API_KEY')

agent_name = "OpenAI (API Key)"
pswd = os.getenv('OPENAI_API_KEY')
agent = OpenAiAgent(model="text-davinci-003", api_key=pswd)
print("OpenAI is initialized 💪")

boat = agent.run("Generate an image of a boat in the water")
print(boat)


caption = agent.run("Can you caption the `boat_image`?", boat_image=boat)
print(caption)