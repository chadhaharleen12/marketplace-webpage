import streamlit as st
st.markdown(
    """
    <style>
        .stButton>button {
            width: 100%;
            padding: 1px;
            font-size: 18px;
            background-color: ;
            border: none;
            border-radius: 10px;
            margin-bottom: none;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stButton>button:hover {
            background-color: ;
        }

        .stButton {
            margin-top: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.image("logo.png", use_container_width=True)

tile_1 = st.sidebar.button("Foreign Exchange Rate")
tile_2 = st.sidebar.button("Banking Analytics")
tile_3 = st.sidebar.button("Covid 19")
tile_4 = st.sidebar.button("Demographics")


if tile_1:
    import fer  
elif tile_2:
    import banking 
elif tile_3:
    import covid  
elif tile_4:
    import demographics 