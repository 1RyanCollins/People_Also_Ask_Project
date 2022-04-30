import people_also_ask
import streamlit as st



st.title("People Also Ask Project")
st.text ("Enter a Query and See What People Also Asked on Google")

query = st.text_input("Write Your Query")

for question in people_also_ask.generate_related_questions("cofee")





