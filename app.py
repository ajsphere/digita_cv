import streamlit as st
from PIL import Image
import lessons

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | "
PAGE_ICON = ":wave:"
NAME = "Ajshe Berisha"

DESCRIPTION = """
Computer Science Engineer - Student
"""

EMAIL = "berishaajshe07@gmail.com"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Files
resume_file = "assets/CV_Ajshe_Berisha.pdf"
profile_pic_file = "assets/profile.png"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)


# Sidebar navigation
page = st.sidebar.radio(
    "Navigate",
    ["Home", "About", "Lessons"]
)

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
            mime="application/pdf",
        )


    # --- ABOUT PREVIEW ---
    st.write("")
    st.subheader("About Me")

    st.write("""
    As a technology enthusiast with a passion for innovation, I am a Computer Science & Engineering student who enjoys transforming ideas into practical solutions.
I am constantly exploring software development, data, and emerging technologies while expanding my skills through hands-on projects.
 Driven by creativity and continuous learning, I aim to build meaningful digital experiences that create real impact.

    """)


    # --- SKILLS ---
    st.write("")
    st.subheader("Hard Skills")

    st.write("""
- Programming: Java, Python, SQL
- Tools: GitHub, VS Code, Streamlit
""")


    st.write("")
    st.write("🚧 **Computer Science Engineer | UBT Prizren**")


elif page == "About":

    st.title("About Me")

    st.write("""

I am currently pursuing a Bachelor's degree in **Computer Science & Engineering**, where I am building my knowledge in programming, software development, and core computer science concepts.

Seeking to expand my learning beyond the classroom, I joined a **Data Science & AI** training program that provided hands-on experience through real-world projects. During the program, I worked with Python, SQL, GitHub, Databricks, Streamlit, and data analysis while strengthening my ability to collaborate and solve practical problems.

I enjoy challenging myself through new projects and continuously developing my technical skills. As I progress in my studies, I look forward to gaining industry experience, working on meaningful software projects, and continuing to grow both academically and professionally.

    """)

    st.write("📫", EMAIL)


elif page == "Lessons":
    lessons.show_lessons()