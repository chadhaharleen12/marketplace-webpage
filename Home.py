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

st.text("On this website, you can find the original source links from which our meticulously curated datasets are drawn. For every dataset, we provide direct links to these authentic sources, allowing you to explore the data in detail, verify its accuracy, and gain a comprehensive understanding of its context. With InSights, you gain not only access to powerful datasets but also the tools to navigate and interpret them, ensuring transparency, credibility, and the highest quality insights.")

st.text("Unlock the full potential of your data, elevate your decision-making, and stay ahead of the curve with InSights – where data meets clarity, and insights drive success.")