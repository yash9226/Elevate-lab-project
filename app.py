import pickle
import streamlit as st
import pandas as pd

# ------------------- Load data -------------------
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity_dict.pkl', 'rb'))

# ------------------- Recommend Function -------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[movie_id].title)

    return recommended_movies

# ------------------- Streamlit App -------------------
st.set_page_config(page_title="Movie Recommender", layout="centered")

# ------------------- Custom CSS -------------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
        background: linear-gradient(to bottom, #e0ecfc, #f9fbfe);
    }

    .stApp {
        max-width: 800px;
        margin: auto;
        padding: 2rem 1rem;
    }

    .title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        color: #3a3a3a;
        margin-bottom: 1rem;
        background: linear-gradient(90deg, #845ec2, #00c9a7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .selectbox-label {
        font-size: 20px;
        font-weight: 600;
        color: #333;
        margin-bottom: 0.5rem;
    }

    .recommend-header {
        font-size: 26px;
        font-weight: bold;
        color: #222;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }

    .movie-card {
        background-color: #ffffff;
        padding: 1rem 1.2rem;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.08);
        margin: 0.5rem 0;
        font-size: 18px;
        font-weight: 500;
        color: #1e1e1e;
        transition: transform 0.2s;
    }

    .movie-card:hover {
        transform: scale(1.02);
        background-color: #f2f8ff;
    }

    .stButton > button {
        background-color: #845ec2;
        color: white;
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
        font-size: 16px;
        font-weight: 600;
        border: none;
        transition: 0.3s ease;
        box-shadow: 0 4px 8px rgba(132, 94, 194, 0.3);
    }

    .stButton > button:hover {
        background-color: #6a3fb5;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# ------------------- Title -------------------
st.markdown('<div class="title">🎬 Movie Recommender System</div>', unsafe_allow_html=True)

# ------------------- Selectbox -------------------
st.markdown('<p class="selectbox-label">🔍 Choose a movie:</p>', unsafe_allow_html=True)
selected_movie_name = st.selectbox("", movies['title'].values)

# ------------------- Recommend Button -------------------
if st.button('🎯 Show Recommendation'):
    recommendation = recommend(selected_movie_name)

    st.markdown('<div class="recommend-header">🍿 Top 5 Recommendations:</div>', unsafe_allow_html=True)
    for i in recommendation:
        st.markdown(f"<div class='movie-card'>{i}</div>", unsafe_allow_html=True)
