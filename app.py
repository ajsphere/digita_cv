import streamlit as st
import cv

st.sidebar.title("Menu")

page = st.sidebar.radio("Go to", ["CV", "Projects"])

if page == "CV":
cv.show()

elif page == "Projects":
st.title("Projects")

st.write("Project 1: CV Web App")
st.write("Project 2: Data Analysis")
st.write("Project 3: Python App")
