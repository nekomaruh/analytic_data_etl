import pandas as pd
import numpy as np
import re
import time

start_time = time.time()

df = pd.read_excel("sies.xlsx")
df_len = df['CODIGO UNICO DE CARRERA'].count()

no_data =  'nan'

def cleanDigit(input):
    input = str(input)
    if not input:
        return 0
    if '-' in input:
        return 0
    if 'nan' in input:
        return no_data
    if 's/i' in input:
        return no_data
    return int(float(input))

def cleanText(input):
    input = str(input)
    if ',' in input:
        input = input.replace(',','.')
    if 'nan' in input:
        return no_data
    if 's/i' in input:
        return no_data
    return input

def cleanPercentages(input):
    input = str(input)
    if not input:
        return 0
    if 'nan' in input:
        return no_data
    return 0

def cleanDecimal(input):
    input = str(input)
    if not input:
        return 0.0
    if 'nan' in input:
        return no_data
    if '-' in input:
        return no_data
    if 's/i' in input:
        return no_data
    if input == ' ':
        return no_data
    return float(input)

def cleanPCobertura(input):
    input = str(input)
    if '-' in input:
        return no_data, no_data
    input = input.replace("% <= X <",",")
    input = input.replace("=","")
    input = input.rstrip('%')
    values = input.split(',')
    return int(values[0]), int(values[1])

# Eliminar las columnas que no se van a utilizar
df = df.drop(columns=['TIPO DE INSTITUCION', 'AÑO_DURAC', 'TOTAL MATRICULA','TOTAL MATRICULA 1ER AÑO','TOTAL TITULADOS'])

# Eliminar filas para hacer pruebas
#df = df[:-20920]
#a = df.iloc[:,5].tolist()

# Generar una instanciacion de las columnas a modificar
aa = df["ARANCEL ANUAL"].tolist()
ct = df["COSTO TITULACION"].tolist()
nc = df["NIVEL CARRERA O TIPO DE CARRERA"].tolist()
nca = df["NOMBRE CARRERA"].tolist()

am = df["AÑO MATRÍCULA"].tolist()
tmf = df["TOTAL MATRICULA FEMENINO"].tolist()
tmm = df["TOTAL MATRICULA MASCULINO"].tolist()
m1f = df["MATRICULA DE 1ER AÑO FEMENINO"].tolist()
m1m = df["MATRICULA 1ER AÑO MASCULINO"].tolist()

pmm = df["MATRÍCULA - % DE MUNICIPAL"].tolist()
pmps = df["MATRÍCULA - % DE PARTICULAR SUBVENCIONADO"].tolist()
pmpp = df["MATRÍCULA - % DE PARTICULAR PAGADO"].tolist()
cad = df["C. Administración Delegada"].tolist()

tf = df["TITULADOS FEMENINO"].tolist()
tm = df["TITULADOS MASCULINO"].tolist()

pcpsum1 = df["% DE COBERTURA PSU EN MATRICULA 1ER AÑO "].tolist()
pcpsum1min = []
pcpsum1max = []

ppsum1 = df["PROMEDIO PSU EN MATRICULA 1ER AÑO"].tolist()
pnemm = df["PROMEDIO NEM EN MATRICULA"].tolist()

v1s = df["VACANTES 1ER SEMESTRE"].tolist()

r1a = df["Retención de 1er año"].tolist()
drs = df["Duración real (semestres)"].tolist()
e1a = df["Empleabilidad al 1er año"].tolist()
ip4t = df["Ingreso promedio al 4° año de titulación"].tolist()

acg = df["Área Carrera Genérica"].tolist()

for i in range(len(aa)):
    aa[i] = cleanDigit(aa[i])
    ct[i] = cleanDigit(ct[i])
    nc[i] = cleanText(nc[i])
    nca[i] = cleanText(nca[i])
    
    am[i] = cleanDigit(am[i])
    tmf[i] = cleanDigit(tmf[i])
    tmm[i] = cleanDigit(tmm[i])
    m1f[i] = cleanDigit(m1f[i])
    m1m[i] = cleanDigit(m1m[i])
    
    pmm[i] = cleanDecimal(pmm[i])
    pmps[i] = cleanDecimal(pmps[i])
    pmpp[i] = cleanDecimal(pmpp[i])
    cad[i] = cleanDecimal(cad[i])
    
    tf[i] = cleanDigit(tf[i])
    tm[i] = cleanDigit(tm[i])
    
    mini, maxi = cleanPCobertura(pcpsum1[i])
    pcpsum1min.append(mini)
    pcpsum1max.append(maxi)
    
    ppsum1[i] = cleanDecimal(ppsum1[i])
    pnemm[i] = cleanDecimal(pnemm[i])
    
    v1s[i] = cleanDigit(v1s[i])
    
    r1a[i] = cleanDecimal(r1a[i])
    drs[i] = cleanDecimal(drs[i])
    e1a[i] = cleanDecimal(e1a[i])
    ip4t[i] = cleanText(ip4t[i])
    
    acg[i] = cleanText(acg[i])
    
    
# Asignar las columnas filtradas al dataframe

df["ARANCEL ANUAL"] = aa
df["COSTO TITULACION"] = ct
df["NIVEL CARRERA O TIPO DE CARRERA"] = nc
df["NOMBRE CARRERA"] = nca

df["AÑO MATRÍCULA"] = am
df["TOTAL MATRICULA FEMENINO"] = tmf
df["TOTAL MATRICULA MASCULINO"] = tmm
df["MATRICULA DE 1ER AÑO FEMENINO"] = m1f
df["MATRICULA 1ER AÑO MASCULINO"] = m1m

df["MATRÍCULA - % DE MUNICIPAL"] = pmm
df["MATRÍCULA - % DE PARTICULAR SUBVENCIONADO"] = pmps
df["MATRÍCULA - % DE PARTICULAR PAGADO"] = pmpp
df["C. Administración Delegada"] = cad

df["TITULADOS FEMENINO"] = tf
df["TITULADOS MASCULINO"] = tm

df["% DE COBERTURA PSU EN MATRICULA 1ER AÑO "] = pcpsum1
df["% COBERTURA MIN"] = pcpsum1min
df["% COBERTURA MAX"] = pcpsum1max

df["PROMEDIO PSU EN MATRICULA 1ER AÑO"] = ppsum1
df["PROMEDIO NEM EN MATRICULA"] = pnemm

df["VACANTES 1ER SEMESTRE"] = v1s

df["Retención de 1er año"] = r1a
df["Duración real (semestres)"] = drs
df["Empleabilidad al 1er año"] = e1a
df["Ingreso promedio al 4° año de titulación"] = ip4t

df["Área Carrera Genérica"] = acg

# Crear nuevos frames

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
                      'AÑO_INFORM']]

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