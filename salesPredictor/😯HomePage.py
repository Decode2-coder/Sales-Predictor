import streamlit as st
import pickle
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title="Sales Prediction",
    page_icon="👋",
)


st.sidebar.title('Made By: ')
st.sidebar.markdown(
"""
- Irfan Ansari
- Devank Shinde
- Ankur Sharma
- Atharva Mahalungekar
"""
)
new_title = '<p style="font-family:sans-serif;text-align: center; color:#F63366; font-size: 30px;">WELCOME🙋‍♂️</p>'
st.markdown(new_title, unsafe_allow_html=True)

st.write('This is a Sales Analysis & Prediction Web App built in Streamlit')
img = Image.open("st.webp")
st.image(img)

st.sidebar.success("Select a page above")
