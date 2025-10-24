# connection_snowflake.py
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import os

def connection_snowflake():
    # Define the path to the private key
    current_directory = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(current_directory, 'rsa_key.p8')

    # Load the private key
    with open(key_path, "rb") as key:
        p_key = serialization.load_pem_private_key(
            key.read(),
            password='123'.encode(),  # Password for the key
            backend=default_backend()
        )

    # Convert the private key to DER format
    pkb = p_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Return connection parameters in a dictionary
    conn_params = {
        'user': 'sanchit.arora@cginfinity.com',
        'account': 'fwb23065',
        'private_key': pkb,
        'warehouse': 'SCT_SARORA_WH',
        'database': 'SCT_HKAUR_DB',
        'schema': 'SCT_HKAUR_SCHEMA'
    }

    return conn_params
