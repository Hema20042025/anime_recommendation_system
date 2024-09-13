                                                               Anime Recommendation System

This is a web-based Anime Recommendation System built using Streamlit. It provides personalized anime recommendations based on a similarity algorithm and integrates the TMDb API to display the recommended anime titles along with their posters.

Features:

Anime Recommendation: Recommends anime titles similar to the user's selected anime.

TMDb API Integration: Displays the title and poster of the recommended anime fetched from TMDb.

Responsive UI: Horizontal display of recommendations with a user-friendly interface.

Content-Based Filtering: Uses a similarity matrix to generate recommendations based on content similarity.

Technologies Used:

Python: Core programming language for logic and data handling.
Streamlit: Web framework used to build the interactive UI.
pandas: Data manipulation library for handling the anime dataset.
TMDb API: Used to fetch anime posters and details.
pickle: For loading precomputed similarity matrices and anime datasets.

Files in the Project:

app.py: Main Streamlit app script.
animes.pkl: Pickle file containing the list of animes.
similarity.pkl: Precomputed similarity matrix for content-based filtering.
requirements.txt: List of dependencies required to run the project.

Acknowledgements:
The recommendation engine is inspired by various content-based filtering approaches.
Posters and additional data are provided by TMDb API.












