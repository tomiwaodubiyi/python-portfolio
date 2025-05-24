import streamlit as st
import pandas
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
#col3 = st.columns(1)

with col1:
    st.image("images/photo.jpeg")
with col2:
    st.title("Babatomiwa Odubiyi")
    content = """
    Hi I'm Babatomiwa! I'm a Network Security Engineer and Python Programmer. 
    """
    st.info(content)
contact_writeup = """ I built this webapp to showcase my portfolio. You can contact me if you have any inquiries 
    and I'll be happy to connect with you.
                    """
st.write(contact_writeup)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write(f"[Source code]({row['url']})")