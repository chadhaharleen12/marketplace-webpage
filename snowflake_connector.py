import logging
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import snowflake.connector

class SnowflakeConnector:
    def __init__(self, conn_params):
        self.rsa_key_file_name = "rsa_key.p8"
        self.key_password = "123"
        self.conn_params = conn_params  # Save connection parameters

    def get_secret_key(self):
        # Insted of this we will have it on key vault
        current_directory = os.path.dirname(os.path.abspath(__file__))
        key_path = os.path.join(current_directory, '', self.rsa_key_file_name)
        return key_path

    def get_secret_password(self, rsa_key):
        with open(rsa_key, "rb") as key:
            password_key= serialization.load_pem_private_key(
                key.read(),
                password=self.key_password.encode(),
                backend=default_backend()
            )
        return password_key
    
    def get_private_key_byte(self, private_key):
        return private_key.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption())

    def connect(self):
        rsa_key = self.get_secret_key()
        private_key = self.get_secret_password(rsa_key)
        private_key_bytes = self.get_private_key_byte(private_key)

        # Use the connection parameters correctly from the dictionary
        self.connection = snowflake.connector.connect(
            user=self.conn_params["user"],
            account=self.conn_params["account"],
            private_key=private_key_bytes,
            warehouse=self.conn_params["warehouse"],
            database=self.conn_params["database"],
            schema=self.conn_params["schema"]
        )
        
        logging.info("Connection established")
        return self.connection

    def disconnect(self):
        if self.connection:
            self.connection.close()
            logging.info("Connection closed")
        else:
            logging.error("No connection found")
