import streamlit as st
from streamlit_extras.app_logo import add_logo

add_logo("logo.png")


fer = st.Page("fer.py", title="Foreign Exchange Rate")
covid = st.Page("covid.py", title="Covid 19")
banking = st.Page("banking.py", title="Banking Analytics")
demographics = st.Page("demographics.py", title="Demographics")

pg = st.navigation([fer, covid, banking, demographics])
pg.run()
