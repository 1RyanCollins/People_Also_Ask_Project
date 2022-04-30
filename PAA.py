import people_also_ask
import streamlit as st



st.title("People Also Ask Project")
st.text ("Enter a Query and See What People Also Asked on Google")

query = st.text_input("Write Your Question")

results = people_also_ask.get_related_questions(query)
results = results.split("?", 1)

st.write(results)







