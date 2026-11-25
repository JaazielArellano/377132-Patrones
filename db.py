import psycopg2
from sqlalchemy import create_engine

def conectar_inegi(nombre_bd="postgres"):
    return psycopg2.connect(
        host="148.231.239.96",
        user="jaaziel",
        password="",
        database=nombre_bd
    )

def conectar(nombre_bd="iin_news"):
    url = f"postgresql+psycopg2://jaaziel:@148.231.239.96:5432/{nombre_bd}"
    engine = create_engine(url)
    return engine.connect()