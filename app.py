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
resume_file = "assets/egezon_cv_12_2024.pdf"
profile_pic_file = "assets/profile-pic.png"

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
            file_name="CV.pdf",
            mime="application/octet-stream",
        )

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")
    st.subheader("Experience & Qualifications")
    st.write(
        """
- ✔️ Extensive experience with spatial-sensor data and algorithm development.
- ✔️ Skilled in Python (FastAPI, Pandas, Numpy), SQL, DBT, and Airflow.
- ✔️ Experienced in visualizing and analyzing sensor data to deliver insights.
- ✔️ Proficient in PowerBI and interactive dashboard development.
"""
    )

    # --- SKILLS ---
    st.write("\n")
    st.subheader("Hard Skills")
    st.write(
        """
- 👩‍💻 Programming: Python (FastAPI, Scikit-learn, Pandas), SQL, DBT
- 📊 Data Visualization: PowerBI, Streamlit
- 🗄️ Databases: Snowflake, AWS, PostgreSQL
- 🤖 Machine Learning: Neural networks, classification algorithms
"""
    )

    st.write("\n")
    st.write("🚧", "**Computer Science Engineer |UBT Prizren**")

- ► Developed and implemented machine learning models for scoring.
- ► Automated daily reports and created data visualizations for stakeholders.
"""
    )

    # --- JOB 7
    st.write("\n")
    st.write("🚧", "**Math and IT Teacher | International School of Prishtina, Prishtina**")
    st.write("09/2015 - 05/2021")
    st.write(
        """
- ► Taught Mathematics, IT, and introductory machine learning.
- ► Served as Vice Principal, showcasing leadership in curriculum development.
- ► Instructed robotics and coding with Python and Scratch.
"""
    )

elif page == "About":
    st.title("About Me")
    st.write("""
    I am a computer science engineer student with a strong passion for IT
    
    Over one year, I am a student in UBT Prizren."

    # Show LinkedIn and Email only on the About page
    st.write("📫", EMAIL)
    st.write(f"Feel free to connect with me on [LinkedIn]({LINKEDIN_URL}).")
