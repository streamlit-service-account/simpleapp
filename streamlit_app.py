import streamlit as st

st.title("Test App!!!")

w1 = st.slider("Label 1", 0, 100, 25, 1)
st.write("Value 1:", w1)

w2 = st.slider("Label 2", 0.0, 100.0, (25.0, 75.0), 0.5)
st.write("Value 2:", w2)

