import os
import streamlit as st
from sqlalchemy import create_engine
from dotenv import load_dotenv
# utils/db.py : connexion à la base de données avec SQLAlchemy et gestion des variables d'environnement

load_dotenv()

@st.cache_resource
def get_engine():

    engine = create_engine(
        f"postgresql+psycopg://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}"
    )

    return engine

engine = get_engine()