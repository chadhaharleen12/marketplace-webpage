import streamlit as st

# Custom CSS to adjust the logo size
st.markdown("""
    <style>
        div[data-testid="stSidebarHeader"] > img, div[data-testid="collapsedControl"] > img {
            height: 6rem;
            width: auto;
        }
        
        div[data-testid="stSidebarHeader"], div[data-testid="stSidebarHeader"] > *,
        div[data-testid="collapsedControl"], div[data-testid="collapsedControl"] > * {
            display: flex;
            align-items: center;
        }
    </style>
""", unsafe_allow_html=True)

st.logo("insights_logo.png")

st.header("Welcome to InSights")
st.text("Welcome to InSights, the pinnacle of global decision-making data by CG Infinity. Our cutting-edge data technology solutions compress data discovery to insights, saving time, effort, and budget. Empower individuals and enterprises to explore, visualize, model, and present data for informed decisions and better business outcomes. Revolutionize your world with InSights!")
st.text("On this website, you can find the source links from which our datasets have been curated.")
st.text("For each dataset, we provide direct links to the original sources. You can explore the data in detail, verify its authenticity, and understand the context.")
