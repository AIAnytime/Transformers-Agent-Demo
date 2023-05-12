from huggingface_hub import login
from transformers import HfAgent
import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_TOKEN = os.getenv('HUGGINGFACE_API_TOKEN')
login(HUGGINGFACE_TOKEN)


agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoder")
print("StarCoder is initialized 💪")

boat = agent.run("Generate an image of a boat in the water")
boat.show()
