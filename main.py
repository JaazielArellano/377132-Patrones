
import os
import pandas as pd
from db import conectar
from consultas import exportar_noticias_negativas_economia

#hacemos la consulta, y almacena el resultado en un CSV:
exportar_noticias_negativas_economia()
