import pandas as pd
import sqlalchemy
import psycopg2
import numpy as np
import re
import time

start_time = time.time()

df = pd.read_excel("sies.xlsx")
df_len = df['CODIGO UNICO DE CARRERA'].count()

no_data =  '-'

def cleanPCobertura(input):
    input = str(input)
    if '-' in input:
        return 0.0, 0.0
    input = input.replace("% <= X <",",")
    input = input.replace("=","")
    input = input.rstrip('%')
    values = input.split(',')
    return int(values[0]), int(values[1])

def cleanDuracionRealSemestres(input):
    input = str(input)
    if '%' in input:
        input = input.replace("%","")
        return float(input) / 100
    if '-' in input:
        return 0.0
    if 's/i' in input:
        return 0.0
    if 's/i' in input:
        return 0.0
    if not input:
        return 0.0
    return float(input)



# Eliminar las columnas que no se van a utilizar
df = df.drop(columns=['TIPO DE INSTITUCION', 'AÑO_DURAC', 'TOTAL MATRICULA','TOTAL MATRICULA 1ER AÑO','TOTAL TITULADOS'])

# Eliminar filas para hacer pruebas
#df = df[:-20920]
#a = df.iloc[:,5].tolist()

# Generar una instanciacion de las columnas a modificar
pcpsum1 = df["% DE COBERTURA PSU EN MATRICULA 1ER AÑO "].tolist()
pcpsum1min = []
pcpsum1max = []

drs = df["Duración real (semestres)"].tolist()

df["ARANCEL ANUAL"].replace({
    "N/A":"-",
    "NULL":"-",
    "S/I":"-"},inplace=True)

df["COSTO TITULACION"] = df["COSTO TITULACION"].replace({
    "-":0},inplace=True)

df["NIVEL CARRERA O TIPO DE CARRERA"].replace({
    "#N/D":"-"},inplace=True)

df["TOTAL MATRICULA FEMENINO"].replace({
    "-":"0",
    ".":""},inplace=True)

df["TOTAL MATRICULA MASCULINO"].replace({
    "-":"0",
    ".":""},inplace=True)

df["MATRICULA DE 1ER AÑO FEMENINO"].replace({
    "-":"0"},inplace=True)

df["MATRICULA 1ER AÑO MASCULINO"].replace({
    "-":"0"},inplace=True)

df["MATRÍCULA - % DE MUNICIPAL"].replace({
    "N/A":"0",
    "NULL":"0"},inplace=True)

df["MATRÍCULA - % DE PARTICULAR SUBVENCIONADO"].replace({
    "N/A":"0",
    "NULL":"0"},inplace=True)

df["MATRÍCULA - % DE PARTICULAR PAGADO"].replace({
    "N/A":"0",
    "NULL":"0"},inplace=True)

df["C. Administración Delegada"].replace({
    "-":"0",
    "NULL":"0"},inplace=True)

df["TITULADOS FEMENINO"].replace({
    "-":"0"},inplace=True)

df["TITULADOS MASCULINO"].replace({
    "-":"0"},inplace=True)

df["PROMEDIO PSU EN MATRICULA 1ER AÑO"].replace({
    "N/A":"0",
    "NULL":"0"},inplace=True)

df["PROMEDIO NEM EN MATRICULA"].replace({
    "N/A":"0",
    "NULL":"0"},inplace=True)

df["VACANTES 1ER SEMESTRE"].replace({
    "NULL":"0",
    "s/i":"0"},inplace=True)


df["Retención de 1er año"].replace({
    "-":"0",
    "s/i":"0",
    "#¡VALOR!":"0",
    "":"0"},inplace=True)

df["Empleabilidad al 1er año"].replace({
    "-":"0",
    "":"0"},inplace=True)

df["Área Carrera Genérica"].replace({
    "#N/D":"-"},inplace=True)

df["Ingreso promedio al 4° año de titulación"].replace({
    "s/i":"-",
    "":"-"},inplace=True)


for i in range(len(df_len)):
    mini, maxi = cleanPCobertura(pcpsum1[i])
    pcpsum1min.append(mini)
    pcpsum1max.append(maxi)
    drs[i] = cleanDuracionRealSemestres(drs[i])


# Crear nuevos frames

df["% DE COBERTURA PSU EN MATRICULA 1ER AÑO "] = pcpsum1
df["% COBERTURA MIN"] = pcpsum1min
df["% COBERTURA MAX"] = pcpsum1max
df["Duración real (semestres)"] = drs

df_titulados = df[['AÑO TITULADOS', 
                   'TITULADOS MASCULINO',
                   'TITULADOS FEMENINO',
                   'CODIGO UNICO DE CARRERA']].copy()

df_carrera = df[['CODIGO UNICO DE CARRERA', 
                 'NOMBRE CARRERA', 
                 'ARANCEL ANUAL', 
                 'COSTO TITULACION', 
                 'AREA DE CONOCIMIENTO', 
                 'DURACION CARRERA FORMAL',
                 'NIVEL CARRERA O TIPO DE CARRERA',
                 'Retención de 1er año',
                 'Duración real (semestres)',
                 'Empleabilidad al 1er año',
                 'Ingreso promedio al 4° año de titulación',
                 'CODIGO DE INSTITUCIÓN']].copy()

df_carrera_sede = df[['CODIGO UNICO DE CARRERA',
                      'SEDE', # Este lo usare como codigo sede
                      'PSU PONDERACION NOTAS EM',
                      'PSU PONDERACION RANKING',
                      'PSU PONDERACION LENGUAJE',
                      'PSU PONDERACION MATEMATICAS',
                      'PSU PONDERACION HISTORIA',
                      'PSU PONDERACION CIENCIAS',
                      'PSU PONDERACION OTROS',
                      'VACANTES 1ER SEMESTRE',
                      'TOTAL MATRICULA FEMENINO',
                      'TOTAL MATRICULA MASCULINO',
                      'AÑO_INFORM']].copy()

df_sede = df[['SEDE', 
              'CODIGO DE INSTITUCIÓN',
              'JORNADA',
              'REGION']].copy()

df_institucion = df[['CODIGO DE INSTITUCIÓN',
                     'INSTITUCION']].copy()

df_matricula = df[['PROMEDIO NEM EN MATRICULA',
                   'CODIGO DE INSTITUCIÓN',
                   'PROMEDIO PSU EN MATRICULA 1ER AÑO',
                   'AÑO MATRÍCULA',
                   'MATRÍCULA - % DE MUNICIPAL',
                   'MATRÍCULA - % DE PARTICULAR SUBVENCIONADO',
                   'MATRÍCULA - % DE PARTICULAR PAGADO',
                   'C. Administración Delegada',
                   '% COBERTURA MIN',
                   '% COBERTURA MAX']].copy()

df_titulados.drop_duplicates(subset="CODIGO UNICO DE CARRERA", inplace=True)
df_titulados.reset_index(drop=True, inplace=True)

df_carrera.drop_duplicates(subset="CODIGO UNICO DE CARRERA", inplace=True)
df_carrera.reset_index(drop=True, inplace=True)

df_sede.drop_duplicates(subset="SEDE", inplace=True)
df_sede.reset_index(drop=True, inplace=True)

df_carrera_sede.drop_duplicates(['CODIGO UNICO DE CARRERA','SEDE'], keep='last')
df_carrera_sede.reset_index(drop=True, inplace=True)

df_institucion.drop_duplicates(subset="CODIGO DE INSTITUCIÓN", inplace=True)
df_institucion.reset_index(drop=True, inplace=True)

df_matricula.drop_duplicates(['CODIGO DE INSTITUCIÓN',
                              'PROMEDIO NEM EN MATRICULA',
                              'AÑO MATRÍCULA',
                              'MATRÍCULA - % DE MUNICIPAL',
                              'MATRÍCULA - % DE PARTICULAR SUBVENCIONADO',
                              'MATRÍCULA - % DE PARTICULAR PAGADO',
                              'C. Administración Delegada'], keep='last')
df_matricula.reset_index(drop=True, inplace=True)

"""
def saveTitulados():
    file = open('titulados.sies', 'w')
    line = ""
    for i in range(len(df_titulados)):
        line += str(i)+','
        line += str(df_titulados['AÑO TITULADOS'][i])+','
        line += str(df_titulados['TITULADOS MASCULINO'][i])+","
        line += str(df_titulados['TITULADOS FEMENINO'][i])+","
        line += str(df_titulados['CODIGO UNICO DE CARRERA'][i])+"\n"
    file.write(line)
    file.close()

def saveCarreras():
    file = open('carreras.sies', 'w')
    line = ""
    for i in range(len(df_carrera)):
        line += str(df_carrera['CODIGO UNICO DE CARRERA'][i])+','
        line += str(df_carrera['NOMBRE CARRERA'][i])+","
        line += str(df_carrera['ARANCEL ANUAL'][i])+","
        line += str(df_carrera['COSTO TITULACION'][i])+","
        line += str(df_carrera['AREA DE CONOCIMIENTO'][i])+","
        line += str(df_carrera['DURACION CARRERA FORMAL'][i])+","
        line += str(df_carrera['NIVEL CARRERA O TIPO DE CARRERA'][i])+","
        line += str(df_carrera['Retención de 1er año'][i])+","
        line += str(df_carrera['Duración real (semestres)'][i])+","
        line += str(df_carrera['Empleabilidad al 1er año'][i])+","
        line += str(df_carrera['Ingreso promedio al 4° año de titulación'][i])+","
        line += str(df_carrera['CODIGO DE INSTITUCIÓN'][i])+"\n"
    file.write(line)
    file.close()
    
def saveSedes():
    file = open('sedes.sies', 'w')
    line = ""
    for i in range(len(df_sede)):
        line += str(df_sede['SEDE'][i])+','
        line += str(df_sede['CODIGO DE INSTITUCIÓN'][i])+","
        line += str(df_sede['JORNADA'][i])+","
        line += str(df_sede['REGION'][i])+"\n"
    file.write(line)
    file.close()
    
def saveCarreraSedes():
    file = open('carrera_sedes.sies', 'w')
    line = ""
    for i in range(len(df_carrera_sede)):
        line += str(df_carrera_sede['SEDE'][i])+','
        line += str(df_carrera_sede['CODIGO UNICO DE CARRERA'][i])+","
        line += str(df_carrera_sede['PSU PONDERACION NOTAS EM'][i])+","
        line += str(df_carrera_sede['PSU PONDERACION RANKING'][i])+","
        line += str(df_carrera_sede['PSU PONDERACION LENGUAJE'][i])+","
        line += str(df_carrera_sede['PSU PONDERACION MATEMATICAS'][i])+","
        line += str(df_carrera_sede['PSU PONDERACION HISTORIA'][i])+","
        line += str(df_carrera_sede['PSU PONDERACION CIENCIAS'][i])+","
        line += str(df_carrera_sede['PSU PONDERACION OTROS'][i])+","
        line += str(df_carrera_sede['VACANTES 1ER SEMESTRE'][i])+","
        line += str(df_carrera_sede['TOTAL MATRICULA FEMENINO'][i])+","
        line += str(df_carrera_sede['TOTAL MATRICULA MASCULINO'][i])+","
        line += str(df_carrera_sede['AÑO_INFORM'][i])+"\n"
    file.write(line)
    file.close()
    
def saveInstitucion():
    file = open('institucion.sies', 'w')
    line = ""
    for i in range(len(df_institucion)):
        line += str(df_institucion['CODIGO DE INSTITUCIÓN'][i])+','
        line += str(df_institucion['INSTITUCION'][i])+"\n"
    file.write(line)
    file.close()
    
def saveMatricula():
    file = open('matricula.sies', 'w')
    line = ""
    for i in range(len(df_matricula)):
        line += str(i)+','
        line += str(df_matricula['PROMEDIO NEM EN MATRICULA'][i])+','
        line += str(df_matricula['CODIGO DE INSTITUCIÓN'][i])+','
        line += str(df_matricula['PROMEDIO PSU EN MATRICULA 1ER AÑO'][i])+','
        line += str(df_matricula['AÑO MATRÍCULA'][i])+','
        line += str(df_matricula['MATRÍCULA - % DE MUNICIPAL'][i])+','
        line += str(df_matricula['MATRÍCULA - % DE PARTICULAR SUBVENCIONADO'][i])+','
        line += str(df_matricula['MATRÍCULA - % DE PARTICULAR PAGADO'][i])+','
        line += str(df_matricula['C. Administración Delegada'][i])+','
        line += str(df_matricula['% COBERTURA MIN'][i])+','
        line += str(df_matricula['% COBERTURA MAX'][i])+"\n"
    file.write(line)
    file.close()

# Exportar datos
saveTitulados()
saveCarreras()
saveSedes()
saveCarreraSedes()
saveInstitucion()
saveMatricula()

# Medimos el tiempo que se demoró en ejecutar el código
print("El código se compiló en %s segundos" % (time.time() - start_time))
"""

html_sede = df_sede.to_html("df_SEDE.html")
html_institucion = df_institucion.to_html("df_INSTITUCION.html")
html_titulados = df_titulados.to_html("df_TITULADOS.html")
html_matricula = df_matricula.to_html("df_MATRICULA.html")
html_carrera = df_carrera.to_html("df_CARRERA.html")

engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5432/SIES_MULTI')
#df_sede.to_sql('sedes',engine)
#df_sede.set_index('SEDE', inplace=False)
df_sede.to_sql('sedes',engine,if_exists='replace',index=False)

df_institucion.to_sql('institucion',engine,if_exists='replace',index=False)
df_titulados.to_sql('titulados',engine,if_exists='replace',index=False)
#df_matricula.to_sql('matricula',engine,if_exists='replace',index=False)

df_carrera.to_sql('carrera',engine,if_exists='replace',index=False)