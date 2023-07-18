import streamlit as st

st.title("Campusx")

col1, col2 =  st.columns(2)

with col1:
    st.image("tulips.jpg")
with col2:
    """
    Campus x is a platform to learn data science. It offers one of the best courses with lots of hands-on projects.
    """
st.header("Courses Offered")
st.subheader("Data Science and Machine Learning")
st.subheader("Data Analysis")
st.subheader("Python")
st.subheader("SQL")
st.subheader("DSA")

st.sidebar.title("Menu")
st.sidebar.markdown("""
- Home
- About
- Contact
""")

