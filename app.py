import streamlit as st
import pandas as pd
import requests
import pickle

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

    # Check if results exist
    if data['results']:
        first_result = data['results'][0]  # Taking the first result as the best match
        return {
            'tmdb_id': first_result['id'],
            'title': first_result.get('name', title),  # Get the name or fallback to original title
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


# Load data
animes_list = pickle.load(open('animes.pkl', 'rb'))
animes = pd.DataFrame(animes_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app
st.title("Anime Recommendation System")

selected_anime_name = st.selectbox('***Select an Anime***', animes['name'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_anime_name)

    # Create columns for horizontal layout
    cols = st.columns(len(recommendations))

    # Display each recommendation in a separate column
    for col, recommendation in zip(cols, recommendations):
        with col:
            st.write(recommendation['title'])
            if recommendation['poster_url']:
                st.image(recommendation['poster_url'], use_column_width=True)
            else:
                st.write("***Poster Not Available***")


import gzip

# Path to your existing pickle file
pickle_file = 'similarity.pkl'
compressed_file = 'updated_similarity.pkl.gz'

# Compress the file and save it
with open(pickle_file, 'rb') as f_in:
    with gzip.open(compressed_file, 'wb') as f_out:
        f_out.writelines(f_in)

print(f"Compressed file saved as: {compressed_file}")
