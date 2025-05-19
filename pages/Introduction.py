import streamlit as st
from PIL import Image

st.title("My practice page")

tab1, tab2 = st.tabs(["📷 IMG_0112.jpeg", "🖼️Is it right?"])

with tab1:
    st.header("Hello")
    image1 = Image.open("images/IMG_0112.jpeg")  # IMG_0112.jpeg
    st.image(image1, caption="첫 번째 이미지", use_column_width=True)

with tab2:
    st.header("두 번째 이미지")
    image2 = Image.open("images/IMG_0113.jpeg")  # 두 번째 이미지 경로
    st.image(image2, caption="두 번째 이미지", use_column_width=True)
