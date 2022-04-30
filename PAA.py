import people_also_ask
import streamlit as st



st.title("People Also Ask Project")
st.text ("Enter a Query")

query = st.text_input("Write Your Query")

#results = people_also_ask.get_related_questions(query)

answer = people_also_ask.get_answer(query)
related = answer.get("related_questions"))

st.write(related)


#st.write(results)







