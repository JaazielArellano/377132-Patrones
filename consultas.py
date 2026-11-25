import os
import pandas as pd
from db import conectar, conectar_inegi

#1ra Consulta (Tabla: noticia + noticia_geo)
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

#2da consulta (Tabla: DENUE_INEGI)

def exportar_denue_microempresas(ruta_csv="denue_microempresas_top10.csv", tamano_bloque=10000):
    """
    Extrae establecimientos únicos (sin IDs duplicados) de 0 a 5 personas
    para las 10 entidades federativas seleccionadas desde la tabla denue_inegi_oficial.
    """
    query = """
        SELECT DISTINCT ON (id)
            id,
            nom_estab,
            per_ocu,
            cve_ent,
            entidad,
            municipio,
            telefono,
            correoelec
        FROM denue_inegi_oficial
        WHERE cve_ent IN (2, 14, 8, 11, 26, 21, 20, 15, 25, 31)
          AND per_ocu = '0 a 5 personas'
        ORDER BY id DESC;
    """

    if os.path.exists(ruta_csv):
        os.remove(ruta_csv)

    primero = True
    total_filas = 0

    with conectar_inegi("postgres") as conn:
        for bloque_df in pd.read_sql_query(query, conn, chunksize=tamano_bloque):
            bloque_df.to_csv(
                ruta_csv,
                mode="w" if primero else "a",
                header=primero,
                index=False,
                encoding="utf-8-sig"
            )
            primero = False
            total_filas += len(bloque_df)

    print(f"Exportación DENUE completada: {total_filas} filas únicas guardadas en '{ruta_csv}'.")