import pandas as pd

df = pd.read_csv("sample_earthquakes.csv")

# Imputar por tipo de variable
num_cols = ['nst', 'gap', 'dmin', 'horizontalError', 'depthError', 'magError', 'magNst']
for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)

# Para variables categóricas
df['place'].fillna('desconocido', inplace=True)

# Guardar
df.to_csv("earthquakes_imputed.csv", index=False)
