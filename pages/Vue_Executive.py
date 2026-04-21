import streamlit as st
import pandas as pd
import plotly.express as px
from utils.queries import run_query
# vue exécutive : KPIs, évolution temporelle, export CSV

st.title(" Vue Executive")

# filtre temporel 
# permet de faire une analyse temporelle dans la vue exécutive et d'avoir des KPIs dynamiques en fonction de l'année sélectionnée  

st.sidebar.header("Filtres")

df = run_query("""
SELECT t.*, tm.date_transaction
FROM transactions t
JOIN temps tm ON t.temps_id = tm.temps_id
""")

df["date_transaction"] = pd.to_datetime(df["date_transaction"])

# filtre année pour analyse temporelle

years = df["date_transaction"].dt.year.unique()
year = st.sidebar.selectbox("Année", sorted(years))

df = df[df["date_transaction"].dt.year == year]

#  KPIs pour la vue exécutive

total_tx = len(df)
ca_total = df["montant_eur"].sum()
clients = df["compte_id"].nunique()
marge = df["montant_eur"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Transactions", total_tx)
col2.metric("CA Total", round(ca_total, 2))
col3.metric("Clients actifs", clients)
col4.metric("Marge moyenne", round(marge, 2))

#  GRAPH EVOLUTION
# ajout mois pour analyse temporelle 

df["month"] = df["date_transaction"].dt.to_period("M").astype(str)

line = df.groupby("month")["montant_eur"].sum().reset_index()

fig = px.line(line, x="month", y="montant_eur", title="Evolution CA")

st.plotly_chart(fig, use_container_width=True)


# Export CSV

st.download_button(
    " Export CSV",
    df.to_csv(index=False),
    "data.csv",
    "text/csv"
)