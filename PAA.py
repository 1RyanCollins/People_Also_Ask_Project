import people_also_ask
import streamlit as st



st.title("People Also Ask Project")
st.text ("Enter a Query and See What People Also Asked on Google")

query = st.text_input("Write Your Query")

result = people_also_ask.get_related_questions(query)


for answer in people_also_ask.get_answer(result):
  st.write(answer)




