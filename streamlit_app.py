import streamlit as st

st.title("Test App!!!")

value = st.slider("Pick a number", 0, 10, 3)
st.write(value)

