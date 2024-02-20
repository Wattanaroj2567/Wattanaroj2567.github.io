import torch
import streamlit as st
from PIL import Image
from diffusers import DiffusionPipeline as DP
h = st.header('Diffusion.AI')
s = st.subheader('เว็บไซต์สำหรับแปลงข้อความเป็นภาพ')
p = st.write('เว็บไซต์นี้แลกมาด้วยหยาดเหงื่อและความอดทน')
text = st.text_input('prompt: ')
if text:
    dp = DP.from_pretrained(
            "runwayml/stable-diffusion-v1-5", 
            torch_dtype=torch.float16)
    image_data = dp(text).images[0]
    image = Image.fromarray(image_data)
    image.show()
    #st.image('https://picsum.photos/400/200')
    b = st.button('จะไปต่อหรือ...')