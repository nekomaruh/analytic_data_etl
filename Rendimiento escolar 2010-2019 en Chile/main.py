import pandas as pd
import time

start_time = time.time()

def read_file(year, drops):
    # Leemos los datos y separamos por ; porque algunos nombres de establecimientos poseen comas y dan error
    df = pd.read_csv("Rendimiento por estudiante "+str(year)+".csv", sep=';', low_memory=False)
    df_len = df['NOM_RBD'].count()

    # Eliminamos columna de Código de sector económico (sólo media técnico-profesional y artística)
    # Eliminamos columna de Código de especialidad (sólo media técnico-profesional y artística)
    # No nos sirve para el análisis de datos final y contienen datos vacíos en algunos casos
    df = df.drop(columns=drops)
    return df

df_2010 = read_file(year=2010, drops=['COD_SEC', 'COD_ESPE'])

import static_tables as st
import queries as q

if __name__ == "__main__":

    q.create_static_tables() # Crea las tablas estáticas
    
    # Inserta los valores a las tablas estáticas
    q.insert_dim_depe(st.data_depe)
    q.insert_dim_region(st.data_region)
    q.insert_dim_provincia(st.data_provincia)
    
    
    # Leemos los archivos
    df_2010 = read_file(year=2010, drops=['COD_SEC', 'COD_ESPE', 'INT_ALU'])
    #df_2011 = read_file(year=2011, drops=['COD_SEC', 'COD_ESPE', 'INT_ALU', 'FEC_ING_ALU'])
    #df_2012 = read_file(year=2012, drops=['COD_SEC', 'COD_ESPE', 'INT_ALU'])

    # Exportamos archivos html para ver si las tablas están bien
    #html_2010 = df_2010.to_html("df_2010.html")

    for col in df_2010.columns: 
        print(col)
        
    print('Termino')
    