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

        lecture = st.selectbox(
            "Choose Lecture",
            [
                "Lecture 1",
                "Lecture 2",
                "Lecture 3"
            ]
        )


        if lecture == "Lecture 1":

            st.markdown("""
## SQL - Structured Query Language

SQL (Structured Query Language) është gjuhë që përdoret për komunikim me databaza.


## Përdorimi i SQL

Me SQL mundemi:

- Të kërkojmë të dhëna nga databaza
- Të shkruajmë të dhëna të reja
- Të përditësojmë të dhënat ekzistuese
- Të fshijmë të dhëna


## Komandat bazë të SQL

- SELECT → merr të dhëna
- INSERT → shton të dhëna
- UPDATE → ndryshon të dhëna
- DELETE → fshin të dhëna


## Tables dhe Views

Tables:
- Ruajnë të dhëna në databazë.

Views:
- Janë rezultate të bazuara në query.


## Relationships në SQL

- One to One
- One to Many
- Many to Many


## Primary Key dhe Foreign Key

Primary Key:
- Identifikues unik për çdo rekord.

Foreign Key:
- Lidh tabela të ndryshme mes vete.
            """)


        elif lecture == "Lecture 2":

            st.subheader("SQL Queries")
            st.write("Summary for Lecture 2 will be added here.")


        elif lecture == "Lecture 3":

            st.subheader("SQL Joins")
            st.write("Summary for Lecture 3 will be added here.")



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