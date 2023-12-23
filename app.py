import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm
from PIL import Image

API_KEY = 'AIzaSyDp7w1aTllF9shGJGW8S8rcmiqVFJJh1KM'
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Generate Blog", 
                   page_icon="📸",
                   layout="centered",
                   initial_sidebar_state='collapsed')

st.header("Generate Blog From Image")

uploaded_file = st.file_uploader("Choose an Image file", type=['jpg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption='Uploaded Image', use_column_width=True)
    bytes_data = uploaded_file.getvalue()

generate = st.button("Generate blog!")

if generate:
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(
        glm.Content(
            parts = [
                glm.Part(text="Write a  engaging blog post based on this picture."),
                glm.Part(
                    inline_data=glm.Blob(
                        mime_type='image/jpeg',
                        data=bytes_data
                    )
                ),
            ],
        ),
        stream=True)

    response.resolve()
    print(response.text)
    st.write(response.text)