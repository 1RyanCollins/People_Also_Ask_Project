import people_also_ask
import streamlit as st


st.title("People Also Ask Link Analysis Project")
st.text ("Enter a Query")

question = st.text_input("Write Your Question")

answer = people_also_ask.get_answer(question)

st.text(answer)








