from dotenv import load_dotenv
import psycopg2 as pg
import os
from datetime import datetime

load_dotenv()

def connect():
    connection = pg.connect(host = 'localhost', user = 'postgres', database = 'MovieData', password = 'postgres')
    return connection


def insertarActor(acName, fcLikes):
    connection = connect()
    cursor = connection.cursor()
    sql = "INSERT INTO actor(actorname,fclikes) VALUES(%s, %s)"
    values = (acName, fcLikes)
    cursor.execute(sql, values)
    connection.commit()






def insertarMovie(link,title,dirName,color,numCrit,duration,dirFcLikes,gross,numVotUser,castTotFcLikes,faceNumber,plotKeyWords,genres,numUserRev,lang,country,aspectR,imdbScore,fcLikes,titleYear,budget,contRating,idAc1,idAc2,idAc3):
    connection = connect()
    cursor = connection.cursor()
    sql = "INSERT INTO movie(movielink,movietitle,directorname,color,numcrit,duration,direcfclikes,gross,numvotuser,cattotfclikes,facenumber,plotkeywords,genres,numuserreviews,languag,country,aspectratio,imdbscore,fclikes,titleyear,budget,cotrating,idactor1,idactor2,idactor3) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s )"
    values = (link,title,dirName,color,numCrit,duration,dirFcLikes,gross,numVotUser,castTotFcLikes,faceNumber,plotKeyWords,genres,numUserRev,lang,country,aspectR,imdbScore,fcLikes,titleYear,budget,contRating)
    cursor.execute(sql, values)
    connection.commit()


insertarActor('Leonel Villagra',1900)



def leerActores():
    archivo = open("Movie Data/actors.txt","r")
    linea = archivo.readline().strip()
    while linea != "":
        partes = linea.split(",")
        nombre = partes[0]
        fclikes = partes[1]
        insertarActor(nombre,fclikes)
        linea = archivo.readline().strip()
    leerMovie()



def leerMovie():
    archivo = open("/Movie Data/movies.txt","r")
    linea = archivo.readline().strip()
    while linea != "":
        partes = linea.split(",")
        insertarMovie(partes[0],partes[1],partes[2],partes[3],partes[4],partes[5],partes[6],partes[7],partes[8],partes[9],partes[10],partes[11],partes[12],partes[13],partes[14],partes[15],partes[16],partes[17],partes[18],partes[19],partes[20],partes[21],partes[22],partes[23],partes[24])
        
        linea = archivo.readline().strip()



print("Recien empezara")
print("-----------------------------")
inicial = datetime.now()
leerActores()
final = datetime.now()
total = final - inicial
segundos = total.seconds
print("EXITO! con un tiempo de "+ str(segundos)+" segundos")
print("-----------------------------")
