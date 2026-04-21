import streamlit as st
# app.py : page d'accueil du dashboard avec navigation vers les différentes vues (vue exécutive, analyse des risques)

st.set_page_config(
    page_title="FinanceCore Dashboard",
    layout="wide"
)

st.title("FinanceCore SA Dashboard")

st.sidebar.success("Choisir une page ci-dessus ")

st.write("""
Bienvenue dans le Dashboard FinanceCore :
- Vue Exécutive 
- Analyse des Risques 
""")