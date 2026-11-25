import os
import pandas as pd
from db import conectar

def exportar_noticias_negativas_economia(ruta_csv="noticias_negativas_economia.csv", tamano_bloque=10000):
    """
    Filtra noticias con sentimiento negativo en temas económicos clave,
    incluyendo entidad federativa y municipio, y guarda el resultado en un CSV por bloques.
    """
    query = """
        SELECT 
            n.id_noticia,
            n.titulo,
            n.resumen,
            n.fecha_publicacion,
            n.tema,
            n.sentimiento,
            ng.cve_ent,
            ng.cve_mun
        FROM noticia n
        INNER JOIN noticia_geo ng ON n.id_noticia = ng.id_noticia
        WHERE n.tema IN ('cierre de negocios', 'empleo', 'inversión', 'precios')
          AND n.sentimiento < 0;
    """
    
    # Si el archivo ya existe de una corrida anterior, lo borramos para no duplicar filas
    if os.path.exists(ruta_csv):
        os.remove(ruta_csv)

    primero = True
    total_filas = 0

    with conectar("lin_news") as conn:
        for bloque_df in pd.read_sql_query(query, conn, chunksize=tamano_bloque):
            bloque_df.to_csv(
                ruta_csv,
                mode="w" if primero else "a",
                header=primero,
                index=False,
                encoding="utf-8-sig" # Evita problemas con acentos (ej. "inversión") al abrir en Excel
            )
            primero = False
            total_filas += len(bloque_df)

    print(f"Exportación completada: {total_filas} filas guardadas en '{ruta_csv}'.")