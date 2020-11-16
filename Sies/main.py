import pandas as pd
import numpy as np
import re

df = pd.read_excel("sies.xlsx")
data_len = df['director_name'].count()

no_data = 'UNKNOWN'

def cleanColor(input):
    input = str(input)
    input = input.lstrip()
    if 'nan' in input:
        input = no_data
    if '#ERROR' in input:
        input = no_data
    return input

def cleanName(input):
    input = str(input)
    if '#NODATA' in input:
        return no_data
    if 'nan' in input:
        return no_data
    if '?' in input:
        return no_data
    return input.encode("latin-1", 'ignore').decode("utf-8", 'ignore').replace(u'\xa0', u'').strip()

def cleanMovie(input):
    input = str(input)
    input = input[:-1]
    return input

def cleanDigit(input):
    input = str(input)
    if 'nan' in input:
        return 0
    if '#NODATA' in input:
        return 0
    if 'N/I' in input:
        return 0
    return int(float(input))

def cleanDecimal(input):
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
f_color = []
f_director_name = []
f_num_critic_for_reviews = []
f_duration = []
f_director_facebook_likes = []
f_actor_3_facebook_likes = []
f_actor_2_name = []
f_actor_1_facebook_likes = []
f_gross = []
f_genres = []
f_actor_1_name = []
f_movie_title = []
f_num_voted_users = []
f_cast_total_facebook_likes = []
f_actor_3_name = []
f_facenumber_in_poster = []
f_plot_keywords = []
f_movie_imdb_link = []
f_num_user_for_reviews = []
f_language = []
f_country = []
f_content_rating = []
f_budget = []
f_title_year = []
f_actor_2_facebook_likes = []
f_imdb_score = []
f_aspect_ratio = []
f_movie_facebook_likes = []

# Filter (Ver cuanto tiempo se demora en filtrar)
for i in range(data_len):
    f_color.append(cleanColor(color[i]))
    f_director_name.append(cleanName(director_name[i]))
    f_num_critic_for_reviews.append(cleanDigit(num_critic_for_reviews[i]))
    f_duration.append(cleanDigit(duration[i]))
    f_director_facebook_likes.append(cleanDigit(director_facebook_likes[i]))
    f_actor_3_facebook_likes.append(cleanDigit(actor_3_facebook_likes[i]))
    f_actor_2_name.append(cleanName(actor_2_name[i]))
    f_actor_1_facebook_likes.append(cleanDigit(actor_1_facebook_likes[i]))
    f_gross.append(cleanDigit(gross[i]))
    f_genres.append(genres[i]) # No se limpia
    f_actor_1_name.append(cleanName(actor_1_name[i]))
    f_movie_title.append(cleanName(movie_title[i]))
    f_num_voted_users.append(num_voted_users[i]) # No se limpia
    f_cast_total_facebook_likes.append(cast_total_facebook_likes[i]) # No se limpia
    f_actor_3_name.append(cleanName(actor_3_name[i]))
    f_facenumber_in_poster.append(cleanDigit(facenumber_in_poster[i]))
    f_plot_keywords.append(cleanName(plot_keywords[i]))
    f_movie_imdb_link.append(movie_imdb_link[i]) # No se limpia
    f_num_user_for_reviews.append(cleanDigit(num_user_for_reviews[i]))
    f_language.append(language[i]) # No se limpia
    f_country.append(country[i]) # No se limpia
    f_content_rating.append(content_rating[i]) # No se limpia
    f_budget.append(budget[i]) # No se limpia
    f_title_year.append(title_year[i]) # No se limpia
    f_actor_2_facebook_likes.append(cleanDigit(actor_2_facebook_likes[i]))
    f_imdb_score.append(imdb_score[i]) # No se limpia
    f_aspect_ratio.append(cleanDecimal(aspect_ratio[i]))
    f_movie_facebook_likes.append(movie_facebook_likes[i]) # No se limpia


# Replace filtered data
df['color'] = f_color
df['director_name'] = f_director_name
df['num_critic_for_reviews'] = f_num_critic_for_reviews
df['duration'] = f_duration
df['director_facebook_likes'] = f_director_facebook_likes
df['actor_3_facebook_likes'] = f_actor_3_facebook_likes
df['actor_2_name'] = f_actor_2_name
df['actor_1_facebook_likes'] = f_actor_1_facebook_likes
df['gross'] = f_gross
df['genres'] = f_genres
df['actor_1_name'] = f_actor_1_name
df['movie_title'] = f_movie_title
df['num_voted_users'] = f_num_voted_users
df['cast_total_facebook_likes'] = f_cast_total_facebook_likes
df['actor_3_name'] = f_actor_3_name
df['facenumber_in_poster'] = f_facenumber_in_poster
df['plot_keywords'] = f_plot_keywords
df['movie_imdb_link'] = f_movie_imdb_link
df['num_user_for_reviews'] = f_num_user_for_reviews
df['language'] = f_language
df['country'] = f_country
df['content_rating'] = f_content_rating
df['budget'] = f_budget
df['title_year'] = f_title_year
df['actor_2_facebook_likes'] = f_actor_2_facebook_likes
df['imdb_score'] = f_imdb_score
df['aspect_ratio'] = f_aspect_ratio
df['movie_facebook_likes'] = f_movie_facebook_likes

# Modify values from tables (num_voted_users & cast_total_facebook_likes)
list_imdb = list(set(f_movie_imdb_link))

sum_num_voted_users = [0]*len(list_imdb)
sum_cast_total_facebook_likes= [0]*len(list_imdb)

count_num_voted_users = [0]*len(list_imdb)
count_cast_total_facebook_likes= [0]*len(list_imdb)

avg_num_voted_users = [0]*len(list_imdb)
avg_cast_total_facebook_likes = [0]*len(list_imdb)

# Calculate average (Ver cuanto tiempo se demora en calcular el promedio)
for x in range(data_len):
    imdb = f_movie_imdb_link[x]
    for y in range(len(list_imdb)):
        if imdb == list_imdb[y]:
            sum_num_voted_users[y] += f_num_voted_users[x]
            sum_cast_total_facebook_likes[y] += f_cast_total_facebook_likes[x]
            count_num_voted_users[y] += 1
            count_cast_total_facebook_likes[y] +=1
            break

# Agregamos los promedios a la lista (ver cuanto tiempo demora pasar las foreign keys)
for i in range(len(list_imdb)):
    cvu = count_num_voted_users[i]
    cctfl = count_cast_total_facebook_likes[i]
    if cvu != 0:
        avg_num_voted_users[i] = sum_num_voted_users[i]/cvu
    else:
        avg_num_voted_users[i] = 0
    if cctfl != 0:
        avg_cast_total_facebook_likes[i] = sum_cast_total_facebook_likes[i]/cctfl
    else:
        avg_cast_total_facebook_likes[i] = 0

# Reduce dataframe
df.drop_duplicates(subset ="movie_imdb_link", inplace = True)
df.reset_index(drop=True, inplace=True)

# Replace average columns
df['num_voted_users'] = avg_num_voted_users
df['cast_total_facebook_likes'] = avg_cast_total_facebook_likes

print('Datos origniales:',data_len)
print('Datos filtrados:',len(list_imdb))


# ----- CREATE DATAFRAMES FOR DB ------

# Table movie
df_movie = df.copy()

del df_movie['actor_1_facebook_likes']
del df_movie['actor_2_facebook_likes']
del df_movie['actor_3_facebook_likes']

# Table actors
df_actors1 = df.copy()
df_actors1= df.filter([
    'actor_1_facebook_likes',
    'actor_1_name'], axis=1)

df_actors1.drop_duplicates(subset ="actor_1_name", inplace = True)
df_actors1.reset_index(drop=True, inplace=True)

df_actors2 = df.copy()
df_actors2= df.filter([
    'actor_2_facebook_likes',
    'actor_2_name'], axis=1)

df_actors2.drop_duplicates(subset ="actor_2_name", inplace = True)
df_actors2.reset_index(drop=True, inplace=True)

df_actors3 = df.copy()
df_actors3= df.filter([
    'actor_3_facebook_likes',
    'actor_3_name'], axis=1)

df_actors3.drop_duplicates(subset ="actor_3_name", inplace = True)
df_actors3.reset_index(drop=True, inplace=True)

df_actors1 = df_actors1.rename(columns = {'actor_1_name': 'actor', 'actor_1_facebook_likes': 'likes'}, inplace = False)
df_actors2 = df_actors2.rename(columns = {'actor_2_name': 'actor', 'actor_2_facebook_likes': 'likes'}, inplace = False)
df_actors3 = df_actors3.rename(columns = {'actor_3_name': 'actor', 'actor_3_facebook_likes': 'likes'}, inplace = False)

frames_actors = [df_actors1, df_actors2, df_actors3]

df_actors = pd.concat(frames_actors)
df_actors.drop_duplicates(subset ="actor", inplace = True)
df_actors.reset_index(drop=True, inplace=True)

actor1 = df_movie['actor_1_name']
actor2 = df_movie['actor_2_name']
actor3 = df_movie['actor_3_name']

# Agregamos todos los actores sin  a la tabla (Esta es la parte que mas demora)
for x in range(len(list_imdb)):
    r1_actor = actor1[x]
    r2_actor = actor2[x]
    r3_actor = actor3[x]

    for y in range(len(df_actors)):
        if df_actors['actor'][y] == r1_actor:
            actor1[x] = y
            break
    
    for y in range(len(df_actors)):
        if df_actors['actor'][y] == r2_actor:
            actor2[x] = y
            break
    
    for y in range(len(df_actors)):
        if df_actors['actor'][y] == r3_actor:
            actor3[x] = y
            break

df_movie['actor_1_name'] = actor1
df_movie['actor_2_name'] = actor2
df_movie['actor_3_name'] = actor3

# Export actors.txt
def saveActors():
    file = open('actors.txt', 'w')
    line = ""
    for i in range(len(df_actors)):
        line += str(i)+","+str(df_actors['actor'][i])+","+str(df_actors['likes'][i])+"\n"
    file.write(line)
    file.close()

# Export movies.txt
def saveMovies():
    file = open('movies.txt', 'w')
    line = ""
    for i in range(len(df_movie)):
        line += str(df_movie['movie_imdb_link'][i]) + ','
        line += str(df_movie['movie_title'][i])+","
        line += str(df_movie['director_name'][i])+","
        line += str(df_movie['color'][i])+","
        line += str(df_movie['num_critic_for_reviews'][i])+','
        line += str(df_movie['duration'][i])+','
        line += str(df_movie['director_facebook_likes'][i])+","
        line += str(df_movie['gross'][i])+","
        line += str(df_movie['num_voted_users'][i])+","
        line += str(df_movie['cast_total_facebook_likes'][i])+","
        line += str(df_movie['facenumber_in_poster'][i])+","
        line += str(df_movie['plot_keywords'][i])+","
        line += str(df_movie['genres'][i])+","
        line += str(df_movie['num_user_for_reviews'][i])+","
        line += str(df_movie['language'][i])+","
        line += str(df_movie['country'][i])+","
        line += str(df_movie['aspect_ratio'][i])+","
        line += str(df_movie['imdb_score'][i])+","
        line += str(df_movie['movie_facebook_likes'][i])+","
        line += str(df_movie['title_year'][i])+","
        line += str(df_movie['budget'][i])+","
        line += str(df_movie['content_rating'][i])+","
        line += str(df_movie['actor_1_name'][i])+","
        line += str(df_movie['actor_2_name'][i])+","
        line += str(df_movie['actor_3_name'][i])+"\n"
    file.write(line)
    file.close()

# Exportar datos
#saveActors()
#saveMovies()