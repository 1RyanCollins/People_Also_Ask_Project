import people_also_ask
import streamlit as st


title("People Also Ask Link Analysis Project")

question = st.text_input("Write Your Question")

x = people_also_ask.get_answer(question)

st.write(x)











