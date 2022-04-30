import people_also_ask
import streamlit as st

[theme]
base="light"

st.title("People Also Ask Project")


result = people_also_ask.get_related_questions("coffee")

st.write(result)




