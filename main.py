import pandas as pd
import numpy as np
import re


df = pd.read_excel("moviedata.xlsx")
cant_datos = df['director_name'].count()

no_data = 'UNKNOWN'



def limpiarColor(input):
    input = str(input)
    input = input.lstrip()
    if 'nan' in input:
        input = no_data
    if '#ERROR' in input:
        input = no_data
    return input

def limpiarNombre(input):
    input = str(input)
    if '#NODATA' in input:
        return no_data
    if 'nan' in input:
        return no_data
    if '?' in input:
        return no_data
    return input.encode("latin-1", 'ignore').decode("utf-8", 'ignore')

def limpiarDigito(input):
    input = str(input)
    if 'nan' in input:
        return 0
    if '#NODATA' in input:
        return 0
    if 'N/I' in input:
        return 0
    return int(float(input))

def limpiarDecimal(input):
    input = str(input)
    if 'nan' in input:
        return 0
    return float(input)

# Datos
color = df['color']
director_name = df['director_name']
num_critic_for_reviews = df['num_critic_for_reviews']
duration = df['duration']
director_facebook_likes = df['director_facebook_likes']
actor_3_facebook_likes = df['actor_3_facebook_likes']
actor_2_name = df['actor_2_name']
actor_1_facebook_likes = df['actor_1_facebook_likes']
gross = df['gross']
genres = df['genres']
actor_1_name = df['actor_1_name']
movie_title = df['movie_title']
num_voted_users = df['num_voted_users']
cast_total_facebook_likes = df['cast_total_facebook_likes']
actor_3_name = df['actor_3_name']
facenumber_in_poster = df['facenumber_in_poster']
plot_keywords = df['plot_keywords']
movie_imdb_link = df['movie_imdb_link']
num_user_for_reviews = df['num_user_for_reviews']
language = df['language']
country = df['country']
content_rating = df['content_rating']
budget = df['budget']
title_year = df['title_year']
actor_2_facebook_likes = df['actor_2_facebook_likes']
imdb_score = df['imdb_score']
aspect_ratio = df['aspect_ratio']
movie_facebook_likes = df['movie_facebook_likes']

# Filtros
f_colors = []



for i in range(cant_datos):
    f_color = limpiarColor(color[i])
    print(f_color)
    #f_colors.append(f_color)
    
    #f_director = limpiarNombre(director_name[i])
    #print(f_director)

    #f_ncfr = limpiarDigito(num_critic_for_reviews[i])
    #print(f_ncfr)

    #f_duration = limpiarDigito(duration[i])
    #print(f_duration)

    #f_dfl = limpiarDigito(director_facebook_likes[i])
    #print(f_dfl)

    #f_a3fl = limpiarDigito(actor_3_facebook_likes[i])
    #print(f_a3fl)

    #f_a2n = limpiarNombre(actor_2_name[i])
    #print(f_a2n)

    #f_a1fl = limpiarDigito(actor_1_facebook_likes[i])
    #print(f_a1fl)

    #f_gross = limpiarDigito(gross[i])
    #print(f_gross)

    # La columna genres no se limpia

    #f_a1n = limpiarNombre(actor_1_name[i])
    #print(f_a1n)

    #f_mt = limpiarNombre(movie_title[i])
    #print(f_mt)

    # La columna num_voted_users no se limpia
    # La columna cast_total_facebook_likes no se limpia
    
    #f_a3n = limpiarNombre(actor_3_name[i])
    #print(f_a3n)

    #f_fip = limpiarDigito(facenumber_in_poster[i])
    #print(f_fip)

    #f_pk = limpiarNombre(plot_keywords[i])
    #print(f_pk)

    # La columna movie_imdb_link no se limpia

    #f_nufr = limpiarDigito(num_user_for_reviews[i])
    #print(f_nufr)

    # La columna language no se limpia
    # La columna country no se limpia
    # La columa content_rating no se limpia
    # La columna budget no se limpia
    # La columna title_year no se limpia

    #f_a2fl = limpiarDigito(actor_3_facebook_likes[i]) # Vacios
    #print(f_a2fl)

    # La columna imdb_score no se limpia
    
    #f_ar = limpiarDecimal(aspect_ratio[i]) # Vacios
    #print(f_ar)

    # La columna movie_facebook_likes no se limpia
    #print(0)





    


"""
for i in range(len(actor_1_facebook_likes)):
    actor = str(actor_3_name[i])
    if actor == ' ':
        print("vacio")

"""