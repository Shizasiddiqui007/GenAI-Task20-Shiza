import pandas as pd
import re
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords', quiet=True)

# loading data
df = pd.read_csv('movies.csv')

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = [w for w in text.split() if w not in stop_words]
    return ' '.join(words)

df['combined'] = df['genre'].fillna('') + ' ' + df['overview'].fillna('')
df['clean_text'] = df['combined'].apply(clean_text)

# tfidf and similarity
tfidf = TfidfVectorizer(max_features=500, ngram_range=(1,2))
tfidf_matrix = tfidf.fit_transform(df['clean_text'])
sim_matrix = cosine_similarity(tfidf_matrix)

def recommend(item_name, top_n=5):
    matches = df[df['title'].str.lower() == item_name.lower()]
    if len(matches) == 0:
        return []
    idx = matches.index[0]
    scores = sorted(list(enumerate(sim_matrix[idx])), key=lambda x: x[1], reverse=True)
    top = scores[1:top_n+1]
    return [df['title'].iloc[i] for i, s in top]

# streamlit UI
st.title('Movie Recommendation System')
st.write('Select a movie and get similar movie recommendations')

movie_list = df['title'].tolist()
selected = st.selectbox('Choose a movie:', movie_list)

if st.button('Get Recommendations'):
    results = recommend(selected)
    if results:
        st.subheader('You might also like:')
        for i, r in enumerate(results, 1):
            st.write(f'{i}. {r}')
    else:
        st.write('no recommendations found')
