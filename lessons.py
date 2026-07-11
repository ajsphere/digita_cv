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
            st.subheader("SQL - Structured Query Language")

            st.markdown("""
            **SQL (Structured Query Language)**

            SQL përdoret për komunikim me databaza.
            Nuk është gjuhë programimi, por gjuhë për menaxhimin
            e të dhënave në formë tabelare.

            **Me SQL mundemi:**
            - Kërkojmë të dhëna
            - Shkruajmë të dhëna
            - Përditësojmë të dhëna
            - Fshijmë të dhëna

            **Data Analyst:**
            - Përdor SQL për analizë dhe marrjen e të dhënave.

            **Data Engineer:**
            - Krijon, menaxhon, pastron dhe përditëson të dhënat.

            **CRUD Operations:**
            - Create
            - Read
            - Update
            - Delete

            **Server → Database → Schema**

            Serveri përmban databaza.
            Brenda databazës gjenden schema.
            Brenda schemave gjenden tabela dhe views.

            **Relationships në SQL:**
            - One to One
            - One to Many
            - Many to Many

            **Keys:**
            - Primary Key: identifikues unik
            - Foreign Key: lidh tabela mes vete

            **Data Warehouse:**
            Të dhëna të organizuara për analiza.

            **Data Lake:**
            Të dhëna të strukturuara dhe jo të strukturuara.

            **Data Mart:**
            Të dhëna për një departament specifik.

            **Star Schema:**
            Një tabelë qendrore me tabela të lidhura.

            **Snowflake Schema:**
            Strukturë më e ndarë dhe e normalizuar.

            **DBMS vs RDBMS**

            DBMS:
            Menaxhon databaza.

            RDBMS:
            Menaxhon të dhëna në tabela me lidhje mes tyre.

            **OLAP:**
            Përdoret për analiza.

            **OLTP:**
            Përdoret për transaksione.

            **VPS:**
            Virtual Private Server.
            """)

        elif lecture == "Lecture 2":
            st.subheader("SQL Queries")
            st.write("Add lesson summary here...")

        elif lecture == "Lecture 3":
            st.subheader("SQL Joins")
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