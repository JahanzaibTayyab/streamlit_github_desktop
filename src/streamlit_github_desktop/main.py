import numpy as np
import streamlit as st

st.header("This is 2nd March Header File")
st.text("Write text without Markdown or HTML parsing.")
st.text_area("Display a multi-line text input widget.")
st.text_input("Display a single-line text input widget.")
st.video("https://youtu.be/KRHg6yZw3r0?si=hetOp5AVkIgLd8zA")


message = st.chat_message("assistant")
message.write("Hello human")
message.bar_chart(np.random.randn(30, 3))
