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
<img width="813" height="345" alt="image" src="https://github.com/user-attachments/assets/868fe538-29be-4650-88bb-bd82da404bd2" />


6. Correr el script principal:
    ```bash 
    py main.py

## Capturas de evidencia
<img width="1306" height="480" alt="image" src="https://github.com/user-attachments/assets/cc5d86f1-2c5b-453b-a8e0-79ccca8f16df" />


<img width="755" height="356" alt="image" src="https://github.com/user-attachments/assets/2ab7cfd6-510e-4986-a2ec-b1d6e56cfe42" />

<img width="746" height="254" alt="image" src="https://github.com/user-attachments/assets/4fa3c9a7-cffc-4b69-894e-7841808a4941" />
(~600 registros)

<img width="754" height="263" alt="image" src="https://github.com/user-attachments/assets/39923717-b78d-4809-b755-23ddfd2badfd" />
(~30k registros)



# Documentacion Metodológica:

<img width="1097" height="1280" alt="image" src="https://github.com/user-attachments/assets/fd2dc6d2-7926-41c2-9261-010549e75c6a" />


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
