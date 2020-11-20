from dotenv import load_dotenv
import psycopg2 as pg
import os
from datetime import datetime

load_dotenv()


connection = pg.connect(host = 'localhost', user = 'postgres', database = 'DataBaseSIES', password = 'postgres')



def insertarCarrera(codigo, nombre, area, niveltipo, arancel, costotitulacion, ingresoprom4año, empleabilidad, duracionreal, porcenreten, duracionformal):
    cursor = connection.cursor()
    sql = "INSERT INTO carrera(codcarrera,nombrecarrera,area,niveltipo,arancel,costotitulacion,ingresprom4año,empleabilidad,duracionreal,porcenreten,duracionformal) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (codigo, nombre, area, niveltipo, arancel, costotitulacion, ingresoprom4año, empleabilidad, duracionreal, porcenreten, duracionformal)
    cursor.execute(sql, values)
    connection.commit()




def insertarInstitucion(codigo, nombre):
    cursor = connection.cursor()
    sql = "INSERT INTO institucion(codinstitucion, nombreinstitucion) VALUES(%s, %s)"
    values = (codigo,nombre)
    cursor.execute(sql, values)
    connection.commit()



def insertarMatricula(promnem, prompsu, añomatricula, porcenmunicipal, porcenparticular, porcenpartsub, porcenadmindelegada, totalprimeraño,codinstitucion):
    cursor = connection.cursor()
    sql = "INSERT INTO matricula(promnem,prompsu,añomatricula,porcenmunicipal,porcenparticular,porcenpartsub,porcenadmindelegada,totalprimeraño,codinstitucion) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (promnem, prompsu, añomatricula, porcenmunicipal, porcenparticular, porcenpartsub, porcenadmindelegada, totalprimeraño,codinstitucion)
    cursor.execute(sql, values)
    connection.commit()



def insertarSede(nombre, jornada, region, codinstitucion):
    cursor = connection.cursor()
    sql = "INSERT INTO sede(nomsede,jornada,region,codinstitucion) VALUES(%s, %s, %s, %s)"
    values = (nombre,jornada,region,codinstitucion)
    cursor.execute(sql, values)
    connection.commit()


def insertarTitulados(año, tituladosmascu, tituladosfeme, codcarrera):
    cursor = connection.cursor()
    sql = "INSERT INTO titulados(añotitulado,tituladomasc,tituladofem,codcarrera) VALUES(%s, %s, %s, %s)"
    values = (año,tituladosmascu,tituladosfeme,codcarrera)
    cursor.execute(sql, values)
    connection.commit()


def insertarCarreraSede(codigoSede, codigoCarrera, ponderacionHist, ponderacionCien, ponderacionLeng, ponderacionMat, ponderacionOtros, totalMatriculaFem, totalMatriculaMasc, ponderacionNEM, vacantes, añoinform):
    cursor = connection.cursor()
    sql = "INSERT INTO carrerasede(codSede, codCarrera, ponderacionhist, ponderacioncien, ponderacionleng, ponderacionmat, ponderacionotros, totalmatriculafem, totalmatriculamasc, ponderacionnem, vacantes, anioInform) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (codigoSede, codigoCarrera, ponderacionHist, ponderacionCien, ponderacionLeng, ponderacionMat, ponderacionOtros, totalMatriculaFem, totalMatriculaMasc, ponderacionNEM, vacantes, añoinform)
    cursor.execute(sql, values)
    connection.commit()



def cambioAInteger(valor):
    valor = 0
    return valor


def cambioAString(valor):
    valor = "-"
    return valor


def leerCarreras():
    archivo = open("Sies/carreras.sies","r")
    linea = archivo.readline().strip()
    while linea != "":
        partes = linea.split(",")
        codigo = partes[0]
        if codigo == "nan":
            codigo = cambioAString(codigo)
        nombre = partes[1]
        if nombre == "nan":
            nombre = cambioAString(nombre)
        arancel = partes[2]
        if arancel == "nan":
            arancel = cambioAInteger(arancel)
        costTitulacion = partes[3]
        if costTitulacion == "nan":
           costTitulacion = cambioAInteger(costTitulacion)
        area = partes[4]
        if area == "nan":
            area = cambioAString(area)
        duracionFormal = partes[5]
        if duracionFormal == "nan":
            duracionFormal = cambioAInteger(duracionFormal)
        nivelTipo = partes[6]
        if nivelTipo == "nan":
            nivelTipo = cambioAString(nivelTipo)
        retencion = partes[7]
        if retencion == "nan":
            retencion = cambioAInteger(retencion)
        duracionReal = partes[8]
        if duracionReal == "nan":
            duracionReal = cambioAInteger(duracionReal)
        empleabilidad = partes[9]
        if empleabilidad == "nan":
            empleabilidad = cambioAInteger(empleabilidad)
        ingresoProm = partes[10]
        if ingresoProm == "nan":
            ingresoProm = cambioAString(ingresoProm)
        insertarCarrera(codigo,nombre,area,nivelTipo,arancel,costTitulacion,ingresoProm,empleabilidad,duracionReal,retencion,duracionFormal)
        linea = archivo.readline().strip()
    leerInstitucion()


def leerInstitucion():
    archivo = open("Sies/institucion.sies","r")
    linea = archivo.readline().strip()
    while linea != "":
        partes = linea.split(",")
        codigo = partes[0]
        nombre = partes[1]
        insertarInstitucion(codigo,nombre)
        linea = archivo.readline().strip()
    leerSedes()



def leerMatricula():
    archivo = open("Sies/matricula.sies","r")
    linea = archivo.readline().strip()
    while linea != "":
        partes = linea.split(",")
        insertarMatricula(partes[0],partes[1],partes[2],partes[3],partes[4],partes[5],partes[6],partes[7],partes[8])
        linea = archivo.readline().strip()
    leerCarreraSede()

def leerSedes():
    archivo = open("Sies/sedes.sies","r")
    linea = archivo.readline().strip()
    while linea != "":
        partes = linea.split(",")
        nombre = partes[0]
        jornada = partes[1]
        region = partes[2]
        codInsti = partes[3]
        insertarSede(nombre,jornada,region,codInsti)
        linea = archivo.readline().strip()
    leerTitulados()


def leerTitulados():
    archivo = open("Sies/titulados.sies","r")
    linea = archivo.readline().strip()
    while linea != "":
        partes = linea.split(",")
        año = partes[0]
        mascu = partes[1]
        fem = partes[2]
        codCarrera = partes[3]
        insertarTitulados(año,mascu,fem,codCarrera)
        linea = archivo.readline().strip()
    leerMatricula()


def leerCarreraSede():
    archivo = open("Sies/carrera_sedes.sies","r")
    linea = archivo.readline().strip()
    while linea != "":
        partes = linea.split(",")
        insertarCarreraSede(partes[0],partes[1],partes[2],partes[3],partes[4],partes[5],partes[6],partes[7],partes[8],partes[9],partes[10],partes[11])
        linea = archivo.readline().strip()





print("Recien empezara")
inicial = datetime.now()
leerCarreras()
final = datetime.now()
total = final - inicial
segundos = total.seconds
print("EXITO! con un tiempo de "+ str(segundos)+" segundos")
