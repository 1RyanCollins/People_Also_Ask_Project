import people_also_ask
import streamlit as st


result = people_also_ask.get_related_questions("coffee")

st.write(result)




