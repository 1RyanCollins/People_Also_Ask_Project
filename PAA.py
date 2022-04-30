import people_also_ask
import streamlit as st



st.title("People Also Ask Project")
query = input()

result = people_also_ask.get_related_questions(query)

st.write(result)




