from dotenv import load_dotenv
import psycopg2 as pg
import os

load_dotenv()


connection = pg.connect(host = 'localhost', user = 'postgres', database = 'DataBaseSIES', password = 'postgres')



def insertarCarrera(codigo, nombre, area, niveltipo, arancel, costotitulacion, ingresoprom4año, empleabilidad, duracionreal, porcenreten, duracionformal):
    cursor = connection.cursor()
    sql = "INSERT INTO carrera(codcarrera,nombrecarrera,area,niveltipo,arancel,costotitulacion,ingres4promanio,empleabilidad,duracionreal,porcenreten,duracionformal) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (codigo, nombre, area, niveltipo, arancel, costotitulacion, ingresoprom4año, empleabilidad, duracionreal, porcenreten, duracionformal)
    cursor.execute(sql, values)
    connection.commit()




def insertarInstitucion(codigo, nombre):
    cursor = connection.cursor()
    sql = "INSERT INTO institucion(codinstitucion, nombreinstitucion) VALUES(%s, %s)"
    values = (codigo,nombre)
    cursor.execute(sql, values)
    connection.commit()



def insertarMatricula(codigo, promnem, prompsu, añomatricula, porcenmunicipal, porcenparticular, porcenpartsub, porcenadmindelegada, totalprimeraño,codinstitucion):
    cursor = connection.cursor()
    sql = "INSERT INTO matricula(codmatricula,promnem,prompsu,añomatricula,porcenmunicipal,porcenparticular,porcenpartsub,porcenadmindelegada,totalprimeraño,codinstitucion) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (codigo, promnem, prompsu, añomatricula, porcenmunicipal, porcenparticular, porcenpartsub, porcenadmindelegada, totalprimeraño,codinstitucion)
    cursor.execute(sql, values)
    connection.commit()



def insertarSede(codigo, nombre, jornada, region, codinstitucion):
    cursor = connection.cursor()
    sql = "INSERT INTO sede(codsede,nomsede,jornada,region,codinstitucion) VALUES(%s, %s, %s, %s, %s)"
    values = (codigo,nombre)
    cursor.execute(sql, values)
    connection.commit()


def insertarTitulados(codigo, año, tituladosmascu, tituladosfeme, codcarrera):
    cursor = connection.cursor()
    sql = "INSERT INTO titulados(codsede,nomsede,jornada,region,codinstitucion) VALUES(%s, %s, %s, %s, %s)"
    values = (codigo,nombre)
    cursor.execute(sql, values)
    connection.commit()


def insertarCarreraSede(codigoSede, codigoCarrera, ponderacionHist, ponderacionCien, ponderacionLeng, ponderacionMat, ponderacionOtros, totalMatriculaFem, totalMatriculaMasc, ponderacionNEM, vacantes, añoinform):
    cursor = connection.cursor()
    sql = "INSERT INTO carrerasede(codSede, codCarrera, ponderacionhist, ponderacioncien, ponderacionleng, ponderacionmat, ponderacionotros, totalmatriculafem, totalmatriculamasc, ponderacionnem, vacantes, añoInform) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (codigoSede, codigoCarrera, ponderacionHist, ponderacionCien, ponderacionLeng, ponderacionMat, ponderacionOtros, totalMatriculaFem, totalMatriculaMasc, ponderacionNEM, vacantes, añoinform)
    cursor.execute(sql, values)
    connection.commit()
