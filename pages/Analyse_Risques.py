import streamlit as st
import pandas as pd
import plotly.express as px
from utils.queries import run_query
import seaborn as sns
import matplotlib.pyplot as plt
# analyse des risques : scatter montant vs score crédit, top clients à risque, corrélation entre score crédit et montant

st.title(" Analyse des Risques")
# requete pour récupérer les données nécessaires à l'analyse des risques

df = run_query("""
SELECT 
    t.compte_id,
    t.montant_eur,
    t.type_operation,
    cl.score_credit_client
FROM transactions t
JOIN comptes c ON t.compte_id = c.compte_id
JOIN clients cl ON c.client_id = cl.client_id
""")

#filtre pour analyse des risques

st.sidebar.header("Filtres Risques")


min_score, max_score = st.sidebar.slider(
    "Score crédit",
    int(df["score_credit_client"].min()),
    int(df["score_credit_client"].max()),
    (300, 850)
)

df = df[
    (df["score_credit_client"] >= min_score) &
    (df["score_credit_client"] <= max_score)
]

# scatter montant vs score crédit pour analyse des risques

fig = px.scatter(
    df,
    x="montant_eur",
    y="score_credit_client",
    color="type_operation",
    title="Risk Analysis"
)

st.plotly_chart(fig, use_container_width=True)

# top clients à risque (montant élevé + score crédit faible)

top = (
    df.groupby("compte_id")["montant_eur"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.write("Top clients à risque")

st.dataframe(top)
st.markdown("Corrélation")

cols = ["score_credit_client", "montant_eur"]

corr = df[cols].corr()

fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="viridis", ax=ax)

st.pyplot(fig)

# export CSV risques 

st.download_button(
    " Export Risques",
    df.to_csv(index=False),
    "risques.csv",
    "text/csv"
)