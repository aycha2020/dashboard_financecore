import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from utils.queries import run_query
# vue exécutive : KPIs, évolution temporelle, export CSV

st.title(" Vue Executive")

# filtre temporel 
# permet de faire une analyse temporelle dans la vue exécutive et d'avoir des KPIs dynamiques en fonction de l'année sélectionnée  

st.sidebar.header("Filtres")

df = run_query("""
SELECT t.*, tm.*, s.segment_client,a.nom_agence
FROM transactions t
JOIN temps tm ON t.temps_id = tm.temps_id
JOIN comptes co ON t.compte_id = co.compte_id
JOIN clients c ON co.client_id = c.client_id
join segments s ON c.segment_id = s.segment_id 
JOIN agences a ON t.agence_id = a.agence_id              
""")

df["date_transaction"] = pd.to_datetime(df["date_transaction"], errors="coerce")
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



#  Graph ligne
st.subheader(" Évolution mensuelle")

#transforme en tableau pour graphique(unstack)

evolution = df.groupby(["mois", "type_operation"])["montant"].sum().unstack()

st.line_chart(evolution)








#  Graph bar
st.subheader(" CA par agence")

st.bar_chart(df.groupby("nom_agence")["montant"].sum())

#  Pie chart
st.subheader(" Répartition des segments")

fig, ax = plt.subplots()
df["segment_client"].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
st.pyplot(fig)


# Export CSV

st.download_button(
    " Export CSV",
    df.to_csv(index=False),
    "data.csv",
    "text/csv"
)


