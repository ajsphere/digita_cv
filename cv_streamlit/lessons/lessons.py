import streamlit as st

def show_lessons():

    st.title("📚 Lessons")

    subject = st.selectbox(
        "Choose a subject",
        [
            "SQL",
            "Data Visualization",
            "Python",
            "Statistics",
            "Machine Learning"
        ]
    )

    if subject == "SQL":
        st.header("🗄️ SQL")
        st.write("Add lesson summary here...")

    elif subject == "Python":
        st.header("🐍 Python")
        st.write("Add lesson summary here...")

    elif subject == "Statistics":
        st.header("📈 Statistics")
        st.write("Add lesson summary here...")

    elif subject == "Machine Learning":
        st.header("🤖 Machine Learning")
        st.write("Add lesson summary here...")

    elif subject == "Data Visualization":
        st.header("📊 Data Visualization")
        st.write("Add lesson summary here...")