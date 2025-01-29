import streamlit as st
from PIL import Image

st.title('テストアプリ')
st.caption('これは動画用のテストアプリです')

# 画像
image = Image.open('./data/banner1_43.png')
st.image(image,width=200)