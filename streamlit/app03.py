import streamlit as st
 
h = st.header('My Web Site on Diffusion')
s = st.subheader('เว็บไซต์ส่วนตัวของผม')
p = st.write('เว็บไซต์แลกมาด้วยหยาดเหงื่อและความอดทน')
#banner = st.image('https://picsum.photos/800/250')
b = st.button('Click me ')
text = st.text_input('prompt: ')
if text:
    st.write(f'การสร้างภาพ.... "(text)"')
    st.image('https://picsum.photos/400/200')
    b = st.button('จะไปต่อหรือ...')

