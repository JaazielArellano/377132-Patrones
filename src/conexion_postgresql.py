import psycopg2

try:
    connection=psycopg2.connect(
        host="148.231.239.96",
        user="jaaziel",
        password="377132",
        database="postgres"
    )

    print("Conexión exitosa")
    cursor=connection.cursor()
    cursor.execute("SELECT version()")
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("conexión cerrada")