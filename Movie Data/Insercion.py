from dotenv import load_dotenv
import psycopg2 as pg
import os

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
    print("Wena")





def insertarMovie(link,title,dirName,color,numCrit,duration,dirFcLikes,gross,numVotUser,castTotFcLikes,faceNumber,plotKeyWords,genres,numUserRev,lang,country,aspectR,imdbScore,fcLikes,titleYear,budget,contRating,idAc1,idAc2,idAc3):
    connection = connect()
    cursor = connection.cursor()
    sql = "INSERT INTO movie(movieLink,movieTitle,directorName,color,numCrit,duration,direcFcLikes,gross,numVotUser,catTotFcLikes,faceNumber,plotKeyWords,genres,numUserReviews,languag,country,aspectRatio,imdbScore,fcLikes,titleYear,budget,cotRating,idActor1,idActor2,idActor3) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, )"
    values = (link,title,dirName,color,numCrit,duration,dirFcLikes,gross,numVotUser,castTotFcLikes,faceNumber,plotKeyWords,genres,numUserRev,lang,country,aspectR,imdbScore,fcLikes,titleYear,budget,contRating)
    cursor.execute(sql, values)
    connection.commit()


insertarActor('Leonel Villagra',1900)


