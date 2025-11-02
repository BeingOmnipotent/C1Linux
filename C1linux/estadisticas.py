import pandas as pd

# Cargar datos limpios
df = pd.read_csv("earthquakes_clean.csv")

# Agrupar por magType y calcular estadísticas descriptivas
stats = df.groupby("magType").agg({
    'latitude': ['mean', 'median', 'min', 'max', 'std'],
    'longitude': ['mean', 'median', 'min', 'max', 'std'],
    'depth': ['mean', 'median', 'min', 'max', 'std'],
    'mag': ['mean', 'median', 'min', 'max', 'std'],
    'nst': ['mean', 'median', 'min', 'max', 'std'],
    'gap': ['mean', 'median', 'min', 'max', 'std'],
    'dmin': ['mean', 'median', 'min', 'max', 'std'],
    'rms': ['mean', 'median', 'min', 'max', 'std'],
    'horizontalError': ['mean', 'median', 'min', 'max', 'std'],
    'depthError': ['mean', 'median', 'min', 'max', 'std'],
    'magError': ['mean', 'median', 'min', 'max', 'std'],
    'magNst': ['mean', 'median', 'min', 'max', 'std']
})

# Aplanar las columnas MultiIndex
stats.columns = ['_'.join(col).strip() for col in stats.columns.values]

# Transponer para que cada variable quede hacia abajo
stats_t = stats.transpose()

# Imprimir resultados
print(stats_t)
