import streamlit as st
import pandas as pd
import requests
import pickle
import gzip

# TMDb API key
tmdb_api_key = '196506d3ecb6b9c36355886bcd6d92ab'

# Function to fetch details from TMDb
def fetch_anime_details(title, api_key):
    url = f'https://api.themoviedb.org/3/search/tv'
    params = {
        'api_key': api_key,
        'query': title
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data['results']:
        first_result = data['results'][0]
        return {
            'tmdb_id': first_result['id'],
            'title': first_result.get('name', title),
            'poster_path': first_result.get('poster_path', None)
        }
    else:
        return None

# Function to get full URL of the poster image
def get_poster_url(poster_path):
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return None

# Function to recommend animes
def recommend(anime):
    anime_index = animes_list[animes_list['name'] == anime].index[0]
    distances = similarity[anime_index]
    anime_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_animes = []
    for i in anime_list:
        anime_name = animes_list.iloc[i[0]]['name']
        details = fetch_anime_details(anime_name, tmdb_api_key)
        if details:
            recommended_animes.append({
                'title': details['title'],
                'poster_url': get_poster_url(details['poster_path'])
            })
        else:
            recommended_animes.append({
                'title': anime_name,
                'poster_url': None
            })
    return recommended_animes

# Load data with compression
animes_list = pickle.load(open('animes.pkl', 'rb'))
animes = pd.DataFrame(animes_list)

# Load the compressed similarity.pkl.gz file
with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)

# Streamlit app
st.title("Anime Recommendation System")

selected_anime_name = st.selectbox('***Select an Anime***', animes['name'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_anime_name)

    cols = st.columns(len(recommendations))
    for col, recommendation in zip(cols, recommendations):
        with col:
            st.write(recommendation['title'])
            if recommendation['poster_url']:
                st.image(recommendation['poster_url'], use_column_width=True)
            else:
                st.write("***Poster Not Available***")




