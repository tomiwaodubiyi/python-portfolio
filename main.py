import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")
with col2:
    st.title("Babatomiwa Odubiyi")
    content = """
    Hi I'm Babatomiwa! I'm a Network Security Engineer and Python Programmer. 
    I built this webapp to showcase my portfolio. You can contact me if you have any inquiries 
    and I'll be happy to connect with you.
    """
    st.info(content)