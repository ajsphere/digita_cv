import streamlit as st

st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to", ["Home", "About", "Projects"])

# HOME (CV)
if page == "Home":
    st.title("Home / CV")

    st.write("Name: Ajshe Berisha")
    st.write("Education: UBT - Computer Science and Engineering")
    st.write("Skills: Python, Streamlit")
    st.write("Email: berishaajshe07@gmail.com")

# ABOUT
elif page == "About":
    st.title("About")

    st.write("This is a simple CV web app built using Streamlit.")

# PROJECTS
elif page == "Projects":
    st.title("Projects")

    st.subheader("Project 1")
    st.write("CV Web App")

    st.subheader("Project 2")
    st.write("Data Analysis Project")

    st.subheader("Project 3")
    st.write("Python Mini App")