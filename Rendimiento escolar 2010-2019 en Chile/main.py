import pandas as pd
#import sqlalchemy
#import psycopg2
import numpy as np
import re
import time

start_time = time.time()

# Leemos los datos y separamos por ; porque algunos nombres de establecimientos poseen comas y dan error
df_2010 = pd.read_csv("Rendimiento por estudiante 2010.csv", sep=';')
df_len = df_2010['NOM_RBD'].count()

# Eliminamos columna de Código de sector económico (sólo media técnico-profesional y artística)
# Eliminamos columna de Código de especialidad (sólo media técnico-profesional y artística)
# No nos sirve para el análisis de datos final y contienen datos vacíos en algunos casos
df_2010 = df_2010.drop(columns=['COD_SEC', 'COD_ESPE', 'INT_ALU'])

print('Termino')
print(df_2010)