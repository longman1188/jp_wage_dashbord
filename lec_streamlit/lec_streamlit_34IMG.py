import streamlit as st
from PIL import Image

#画像を呼び出す
image = Image.open('sample1.jpg')

st.image(image, caption=('IMG1'), use_column_width=True)