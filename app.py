import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | "
PAGE_ICON = ":wave:"
NAME = "Ajshe Berisha"
DESCRIPTION = """
Computer Science Engineer - Student
"""

EMAIL = "berishaajshe07@gmail.com"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Directly reference files in the assets folder (ensure it exists)
resume_file = "assets/CV_Ajshe.pdf"
profile_pic_file = "assets/IMG_8984.jpeg"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "About"])

if page == "Home":
    # --- HERO SECTION ---
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="CV_Ajshe.pdf",
            mime="application/octet-stream",
        )



    # --- SKILLS ---
    st.write("\n")
    st.subheader("Hard Skills")
    st.write(
        """
- Programming : Java, Python
"""
    )

    st.write("\n")
    st.write("🚧", "**Computer Science Engineer |UBT Prizren**")


elif page == "About":
    st.title("About Me")
   st.write("""
    I am a computer science engineer student with a strong passion for IT.
    Over one year, I am a student in UBT Prizren.
    """)
