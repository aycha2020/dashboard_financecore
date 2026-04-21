import pandas as pd
from utils.db import engine
# fonction pour exécuter les requêtes SQL et retourner un DataFrame

def run_query(sql):
    try:
        with engine.connect() as conn:
            df = pd.read_sql(sql, conn)
        return df
    except Exception as e:
        print("SQL Error:", e)
        return pd.DataFrame()