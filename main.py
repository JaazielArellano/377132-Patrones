
import os
import pandas as pd
import plotly.express as px
#from db import conectar
from consultas import exportar_noticias_negativas_economia
from consultas import exportar_denue_microempresas

"""#hacemos la consulta, y almacena el resultado en un CSV:
exportar_noticias_negativas_economia()

#hacemos gráfica acumulativa para encontrar hallazgos
df_noticias_1 = "noticias_negativas_economia.csv"

# 2. Leer el CSV conservando los ceros a la izquierda en las claves geográficas
df = pd.read_csv(df_noticias_1, dtype={"cve_ent": str, "cve_mun": str})

# 3. Agrupar por entidad federativa y tema para contar cuántas noticias hay de cada tipo
df_agrupado = (
    df.groupby(["cve_ent", "tema"])
    .size()
    .reset_index(name="total_noticias")
    .sort_values(by=["cve_ent", "total_noticias"], ascending=[True, False])
)

# 4. Crear el gráfico de barras apiladas (acumulación) con Plotly
fig = px.bar(
    df_agrupado,
    x="cve_ent",
    y="total_noticias",
    color="tema",
    barmode="stack", # Esto apila cada tema uno encima del otro por estado
    title="Acumulación de Noticias Negativas por Entidad Federativa y Tema",
    labels={
        "cve_ent": "Clave de Entidad Federativa",
        "total_noticias": "Cantidad de Noticias",
        "tema": "Categoría / Tema"
    },
    text_auto=True # Muestra el número exacto dentro de cada segmento de la barra
)

# Forzar a que el eje X muestre todas las claves como texto (ej. '02', '08') y no como escala numérica
fig.update_xaxes(type="category")

# Mostrar la gráfica interactiva en tu navegador
fig.show()"""

#hacemos la consulta, y almacena el resultado en un CSV:
exportar_denue_microempresas()