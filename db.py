import psycopg2

def conectar(nombre_bd="postgres"):
    return psycopg2.connect(
        host="148.231.239.96",
        user="jaaziel",
        password="...",
        database=nombre_bd
    )