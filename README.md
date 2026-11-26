# 377132-Patrones
Proyecto integrador entre hojas de cálculo y base de datos ce prueba, comunicación de datos, migración, etc.

# Documentación técnica:
## Instalación y Configuración del Entorno

Este proyecto utiliza un archivo `requirements.txt` para gestionar las dependencias externas necesarias (`pandas`, `plotly`, `psycopg2` y `SQLAlchemy`) y garantizar que el código se ejecute con las mismas versiones con las que fue desarrollado.

### Pasos para ejecutar el proyecto localmente

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/JaazielArellano/377132-Patrones
   
2. **Ubicar los archivos:**
   ```bash 
   cd 377132-Patrones

3. Crear un entonro virtual con python:
    ```bash
    python -m venv venv 
    venv\Scripts\activate

4. Instalar librerías necesarias:
    ```bash
    pip install -r requirements.txt

5. Insertar Password:
    Para que el programa funcione correctamente en la red "**UABC-2.4G**" y se pueda conectar a la base de datos debes insertar la contraseña (**la matrícula del alumno**) en los siguientes espacios.
![image](https://hackmd.io/_uploads/SkUiENSyme.png)

6. Correr el script principal:
    ```bash 
    py main.py

## Capturas de evidencia
![image](https://hackmd.io/_uploads/HJ31HEr1Xx.png)



![image](https://hackmd.io/_uploads/SkmCNErkQg.png)

![image](https://hackmd.io/_uploads/Sk6gSNH1me.png)


# Documentacion Metodológica:
![image](https://hackmd.io/_uploads/rye3HVrk7x.png)

## Consultas PSQL de Análisis

* **Noticias** con **impacto negativo** en la economía de cada estado de la República Mexicana:
```
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
```

* Negocios dentro de los anteriores estados más afectados, que cumplen con requisitos de vulnerabilidad económica y tamaño de empresa:
```
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
```