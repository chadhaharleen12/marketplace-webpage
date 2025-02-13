import streamlit as st
from snowflake_connector import SnowflakeConnector
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import connection_snowflake
from streamlit_extras.app_logo import add_logo

st.markdown("""
    <style>
        div[data-testid="stSidebarHeader"] > img, div[data-testid="collapsedControl"] > img {
            height: 8rem;
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

current_directory = os.path.dirname(os.path.abspath(__file__))
key_path = os.path.join(os.path.dirname(__file__), '..', 'rsa_key.p8')

# Load the RSA private key
with open(key_path, "rb") as key:
    p_key = serialization.load_pem_private_key(
        key.read(),
        password='123'.encode(),  # Password for the key
        backend=default_backend()
    )

    pkb = p_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption())

# Call the connection function and pass schema name
conn_params = connection_snowflake.connection_snowflake()

# Initialize the connector with connection parameters
connector = SnowflakeConnector(conn_params)

# Connect to Snowflake
conn = connector.connect()

# Query the table to fetch data for the selected page
query = f"""
SELECT PAGE_NAME, OVERVIEW, VIEWS_PUBLISHED, SOURCE_LINK, IMAGE_URLS
FROM WEBPAGE_DATA 
WHERE PAGE_NAME = 'Foreign Exchange Rates'
"""

# Execute the query
cursor = conn.cursor()
cursor.execute(query)

# Fetch the data into a Pandas DataFrame
df = cursor.fetch_pandas_all()

# Close the cursor and the connection
cursor.close()
conn.close()

# Check if the data was fetched and display the results
if not df.empty:
    # Display the data in a formatted way
    page_name = df.iloc[0]['PAGE_NAME']
    page_overview = df.iloc[0]['OVERVIEW']
    views_published = df.iloc[0]['VIEWS_PUBLISHED']
    source_link = df.iloc[0]['SOURCE_LINK']
    image_urls = df.iloc[0]['IMAGE_URLS']

    # Show the page overview
    st.title(f"**{page_name} Data**")
    st.header("Overview")
    st.write(page_overview)

    # Show the views published
    st.header("Views Published")
    sections = views_published.split("\n")  # Assuming sections are separated by two newlines
    for section in sections:
        if ':' in section:
            heading, description = section.split(":", 1)
            st.markdown(f"**{heading.strip()}**")  # Make the heading bold
            st.write(description.strip())  # Show the description as plain text

    # Show the source link
    st.header("Source Links")

    # Ensure that image_urls is a list (it might be a string if stored as a CSV-like format in the database)
    # Parsing the string format to a list of URLs if necessary
    if isinstance(image_urls, str):
        image_urls = image_urls.strip("[]").replace('"', '').split(", ")

    # Create a card structure to display the images in a grid

    # Define the CSS for the hover effect, card styling, and center alignment
    st.markdown("""
        <style>
            .card {
                border: 2px solid #ddd;
                border-radius: 8px;
                padding: 10px;
                margin: 10px;
                display: inline-flex;
                justify-content: center;
                align-items: center;
                width:100%;
                max-width: 170px;
                height: 200px;
                text-align: center;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                transition: transform 0.3s ease-in-out;
            }
            .card img {
                width: 250px;
                max-height: 100%;
                border-radius: 5px;
                transition: transform 0.3s ease-in-out;
            }
            .card:hover {
                transform: scale(1.05);
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
            }
            .card-caption {
                font-weight: bold;
                margin-top: 5px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Loop through each image URL and display it inside a card
    for idx, image_url in enumerate(image_urls):
        # Wrap the image inside an anchor tag to make it clickable
        st.markdown(f"""
            <a href="{source_link}" target="_blank">
                <div class="card">
                    <img src="{image_url}" alt="Image {idx+1}">
                </div>
            </a>
        """, unsafe_allow_html=True)

else:
    st.write("No data available for this page.")
