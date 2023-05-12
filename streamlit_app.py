import streamlit as st 
import os 
from transformers.tools import OpenAiAgent
from dotenv import load_dotenv
from huggingface_hub import login
from transformers import HfAgent

load_dotenv()

#Huggingface token management
HUGGINGFACE_TOKEN = os.getenv('HUGGINGFACE_API_TOKEN')
login(HUGGINGFACE_TOKEN)

def huggingface_agent(prompt):
    agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoder")
    st.write("StarCoder is initialized 💪")

    query = agent.run(prompt)
    image_name = 'output_img_huggingface.png'
    query.save(image_name)
    return image_name

#Streamlit Logic
st.title("Transformers Agent Demo")

text_prompt_huggingface = st.text_area("Enter your prompt")
if text_prompt_huggingface is not None:
    if st.button("Run Huggingface Agent"):
        col1, col2 = st.columns([1,1])
        with col1:
            st.info("Your Prompt is: "+text_prompt_huggingface)
        with col2:
            st.info("Generated Image is Below")
            output_image_huggingface = huggingface_agent(text_prompt_huggingface)
            st.image(output_image_huggingface)




