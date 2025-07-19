﻿
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    """Establece y devuelve la conexiÃ³n a la base de datos"""
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error de conexiÃ³n: {err}")
        return None




