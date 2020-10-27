import pandas as pd
import numpy as np
import re

df = pd.read_excel("moviedata.xlsx")
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
    #string = string.replace(u'\xa0', u' ')
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
    f_cast_total_facebook_likes.append(cast_total_facebook_likes) # No se limpia
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

    #f_color = limpiarColor(color[i])
    #print(f_color)
    
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

    #f_mt = cleanName(movie_title[i])
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

    #f_a2fl = limpiarDigito(actor_2_facebook_likes[i]) # Vacios
    #print(f_a2fl)

    # La columna imdb_score no se limpia
    
    #f_ar = limpiarDecimal(aspect_ratio[i]) # Vacios
    #print(f_ar)

    # La columna movie_facebook_likes no se limpia
    #print(0)


"""
print('No se cayó')

# Table color
table_color = list(set(f_color))
print('Colors\n',table_color)

# Table genre
table_genre = list(set(f_genres))
print('Genre\n',table_genre)

# Table plot keywords
table_plot_keywords = list(set(f_plot_keywords))
print('Plot keywords\n',table_plot_keywords)

# Table content rating
table_content_rating = list(set(f_content_rating))
print('Content rating\n',table_content_rating)
"""
# Save filtered data
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
table_movies = list(set(f_movie_title))
print('len table_movies:',len(table_movies))

sum_num_voted_users = [0]*len(table_movies)
sum_cast_total_facebook_likes= [0]*len(table_movies)

count_num_voted_users = [0]*len(table_movies)
count_cast_total_facebook_likes= [0]*len(table_movies)

avg_num_voted_users = [0]*len(table_movies)
avg_cast_total_facebook_likes = [0]*len(table_movies)

# Calculate average
for x in range(data_len):
    movie = f_movie_title[x]
    for y in range(len(table_movies)):
        if movie == table_movies[y]:
            sum_num_voted_users[y] += f_num_voted_users[x]
            sum_cast_total_facebook_likes[y] += f_cast_total_facebook_likes[x]
            count_num_voted_users[y] += 1
            count_cast_total_facebook_likes[y] +=1
            break

# Agregamos los promedios a la lista
for i in range(len(table_movies)):
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
df.drop_duplicates(subset ="movie_title", inplace = True)

# Replace average columns
df['num_voted_users'] = avg_num_voted_users
df['cast_total_facebook_likes'] = avg_cast_total_facebook_likes


# ----- CREATE DATAFRAMES FOR DB ------

# Table colors
df_color = df.filter(['color'], axis=1)
df_color.drop_duplicates(subset ="color", inplace = True)
df_color.reset_index(drop=True, inplace=True)
#print(df_color)

# Table director
df_director_name = df.filter(['director_name'], axis=1)
df_director_name.drop_duplicates(subset ="director_name", inplace = True)
df_director_name.reset_index(drop=True, inplace=True)

# Table country
df_country = df.filter(['country'], axis=1)
df_country.drop_duplicates(subset ="country", inplace = True)
df_country.reset_index(drop=True, inplace=True)

# Table genres
df_genres = df.filter(['genres'], axis=1)
df_genres.drop_duplicates(subset ="genres", inplace = True)
df_genres.reset_index(drop=True, inplace=True)

# Table reviews
df_reviews = df.filter(['num_critic_for_reviews', 'num_user_for_reviews'], axis=1)

# Table plot keywords
df_plot_keywords = df.filter(['plot_keywords'], axis=1)
df_plot_keywords.drop_duplicates(subset ="plot_keywords", inplace = True)
df_plot_keywords.reset_index(drop=True, inplace=True)
print(df_plot_keywords)

# Table content_rating
df_content_rating= df.filter(['content_rating'], axis=1)
df_content_rating.drop_duplicates(subset ="content_rating", inplace = True)
df_content_rating.reset_index(drop=True, inplace=True)
#print(df_content_rating)


# Create dataframe for movies
df_movies = df.filter(['movie_title','budget','title_year','country','genres','plot_keywords'], axis=1)
df_movies.reset_index(drop=True, inplace=True)
df_movies = df_movies.rename(columns = {'country': 'id_country', 'genres': 'id_genres', 'plot_keywords': 'id_keywords'}, inplace = False)

print(df_movies)
for x in range(len(df_movies)):

    # Set index for country
    for y in range(len(df_country)):
        if df_country['country'][y] == df_movies['id_country'][x]:
            df_movies['id_country'][x] = y
            break
    
    # Set index for genres
    for y in range(len(df_genres)):
        if df_genres['genres'][y] == df_movies['id_genres'][x]:
            df_movies['id_genres'][x] = y
            break

    # Set index for reviews (get from movie index)

    # Set index for keywords
    for y in range(len(df_plot_keywords)):
        if df_plot_keywords['plot_keywords'][y] == df_movies['id_keywords'][x]:
            df_movies['id_keywords'][x] = y
            break


print(df_movies)
"""
for i in range(len(df_movies)):
    print(df_movies['country'][i])
"""