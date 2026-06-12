import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ajshe Berisha"
PAGE_ICON = ":wave:"
NAME = "Ajshe Berisha"
DESCRIPTION = "Computer Science Engineering Student"
EMAIL = "berishaajshe07@gmail.com"
LOCATION = "Prizren, Kosovo"
RESUME_FILE = "assets/egezon_cv_12_2024.pdf"
PROFILE_PIC_FILE = "assets/IMG_8984.jpeg"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(RESUME_FILE, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(PROFILE_PIC_FILE)

page = st.sidebar.radio("Navigate", ["Home", "About"])

if page == "Home":
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.write(f"📧 {EMAIL}")
        st.write(f"📍 {LOCATION}")
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="CV.pdf",
            mime="application/octet-stream",
        )

    st.write("\n")
    st.subheader("Professional Summary")
    st.write(
        "Computer Science Engineering Student with a strong passion for IT and software development."
    )

    st.write("\n")
    st.subheader("Hard Skills")
    st.write(
        """
- Programming: Java, Python
- Web: HTML, CSS, JavaScript
- Tools: Git, VS Code
"""
    )

    st.write("\n")
    st.subheader("Experience")
    st.write("🚧 **Computer Science Engineer | UBT Prizren")
    st.write("2025 - Present")
    st.write(
       

    )
elif page == "About":
    st.title("About Me")
    st.write(
        "I am a computer science engineering student with a strong passion for IT. Over one year, I have been a student at UBT Prizren, and I enjoy working on projects that combine technology, learning, and innovation."
    )
