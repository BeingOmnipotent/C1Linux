import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el archivo limpio
df = pd.read_csv("earthquakes_clean.csv")

# 2. Calcular la frecuencia de cada tipo de magnitud
frequency_data = df['magType'].value_counts().sort_values(ascending=False)

# 3. Generar el gráfico de barras
plt.figure(figsize=(10, 6))

# Crear el gráfico
frequency_data.plot(kind='bar', color='skyblue')

# Configurar etiquetas y título
plt.title('Frecuencia de Tipos de Magnitud (magType)')
plt.xlabel('Tipo de Magnitud (magType)')
plt.ylabel('Conteo de Sismos (Frecuencia)')
plt.xticks(rotation=45, ha='right') # Rotar etiquetas para mejor lectura

# Ajustar diseño y guardar en PNG
plt.tight_layout()
plt.savefig('plot_mag_type_bar.png')
