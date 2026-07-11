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
### SQL (Structured Query Language)

SQL është gjuhë që përdoret për komunikim dhe menaxhim të databazave.

SQL nuk është gjuhë programimi, por përdoret për punën me të dhëna në formë tabelare.


### Me SQL mundemi:

- Kërkojmë të dhëna
- Shkruajmë të dhëna
- Përditësojmë të dhëna
- Fshijmë të dhëna


### Data Analyst vs Data Engineer

**Data Analyst**
- Përdor SQL për analizim dhe marrjen e të dhënave.

**Data Engineer**
- Krijon dhe menaxhon sistemet e të dhënave.
- Bën update dhe pastrim të të dhënave.


### CRUD Operations

- Create
- Read
- Update
- Delete


### Server, Database dhe Schema

**Server**
- Infrastrukturë fizike ose virtuale ku ruhen databazat.

**Database**
- Hapësirë virtuale brenda serverit ku ruhen të dhënat.

**Schema**
- Organizim logjik brenda databazës.


### Tables dhe Views

**Tables**
- Ruajnë të dhëna që qëndrojnë në databazë.

**Views**
- Janë rezultate të bazuara në query.


### Relationships në SQL

- One to One
- One to Many
- Many to Many


### Keys

**Primary Key**
- Identifikues unik për rekordet.

**Foreign Key**
- Lidh tabela të ndryshme.


### Star Schema vs Snowflake Schema

**Star Schema**
- Ka një tabelë qendrore dhe tabela të lidhura rreth saj.

**Snowflake Schema**
- Strukturë më e ndarë dhe e normalizuar.


### Data Warehouse

- Të dhëna të organizuara për analiza.


### Data Lake

- Të dhëna të strukturuara dhe jo të strukturuara.


### Data Mart

- Të dhëna për një departament specifik.


### DBMS vs RDBMS

**DBMS**
- Menaxhon databaza.

**RDBMS**
- Menaxhon të dhëna në formë tabelare me lidhje.


### OLAP vs OLTP

**OLAP**
- Përdoret për analiza dhe Data Warehouse.

**OLTP**
- Përdoret për ruajtjen e transaksioneve.


### VPS

Virtual Private Server.
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