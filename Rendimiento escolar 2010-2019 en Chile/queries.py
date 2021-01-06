import psycopg2 as ps

connection = ps.connect(user="postgres", 
                        password="postgres", 
                        database="rendimiento_escolar", 
                        host="localhost", 
                        port="5432")

cursor = connection.cursor()

def create_static_tables():
    
    # Tabla dependencia
    cursor.execute("""CREATE TABLE IF NOT EXISTS dim_depe(
                        COD_DEPE INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        DEPENDENCIA_ESTABLECIMIENTO TEXT NOT NULL);""")
    
    # Tabla región
    cursor.execute("""CREATE TABLE IF NOT EXISTS dim_region(
                        COD_REG_RBD INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        REGION TEXT NOT NULL,
                        REGION_ABREVIADO TEXT NOT NULL
                        );""")
    
    # Tabla provincia
    cursor.execute("""CREATE TABLE IF NOT EXISTS dim_provincia(
                        COD_REG_RBD INTEGER NOT NULL UNIQUE,
                        COD_PRO_RBD INTEGER NOT NULL UNIQUE,
                        PROVINCIA TEXT NOT NULL,
                        primary key(COD_REG_RBD, COD_PRO_RBD),
                        foreign key(COD_REG_RBD) references dim_region(COD_REG_RBD)
                    );""")
    
    # Tabla ruralidad
    cursor.execute("""CREATE TABLE IF NOT EXISTS dim_rural(
                        RURAL_RBD INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        INDICE_RURALIDAD TEXT NOT NULL
                    );""")
    
    # Tabla enseñanza
    cursor.execute("""CREATE TABLE IF NOT EXISTS dim_ense(
                        COD_ENSE INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        DESCRIPCION TEXT NOT NULL
                    );""")
    
    # Tabla grado
    cursor.execute("""CREATE TABLE IF NOT EXISTS dim_grado(
                        COD_ENSE INTEGER NOT NULL UNIQUE,
                        COD_GRADO INTEGER NOT NULL UNIQUE,
                        NOMBRE_GRADO TEXT NOT NULL,
                        primary key(COD_ENSE, COD_GRADO),
                        foreign key(COD_ENSE) references dim_ense(COD_ENSE)
                    );""")
    
    # Tabla genero
    cursor.execute("""CREATE TABLE IF NOT EXISTS dim_genero(
                        GEN_ALU INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        GENERO TEXT NOT NULL
                    );""")
    
    # Tabla situacion final
    cursor.execute("""CREATE TABLE IF NOT EXISTS dim_sit_fin(
                        SIT_FIN TEXT PRIMARY KEY NOT NULL UNIQUE,
                        SITUACION_CIERRE TEXT NOT NULL
                    );""")
    
    # Tabla jornada
    cursor.execute("""CREATE TABLE IF NOT EXISTS dim_jornada(
                        COD_JOR INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        JORNADA TEXT NOT NULL
                    );""")
    
    connection.commit()
    
    print("Tablas agregadas correctamente!")
    
    
def insert_dim_depe(list):
    for i in list:
        cursor.execute("""insert into
        dim_depe(COD_DEPE, DEPENDENCIA_ESTABLECIMIENTO)
        values(%s,%s)""",(i[0], i[1]))
    connection.commit()

def insert_dim_region(list):
    for i in list:
        cursor.execute("""insert into
        dim_region(COD_REG_RBD, REGION, REGION_ABREVIADO)
        values(%s,%s,%s)""",(i[0], i[1], i[2]))
    connection.commit()

def insert_dim_provincia(list):
    for i in list:
        cursor.execute("""insert into
        dim_region(COD_REG_RBD, COD_PRO_RBD, PROVINCIA)
        values(%s,%s,%s)""",(i[0], i[1], i[2]))
    connection.commit()