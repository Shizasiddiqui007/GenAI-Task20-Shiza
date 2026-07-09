# Movie Recommendation System
**Assignment 20 - GenAI Course**
**Name:** Shiza

## About
Content-based movie recommendation system using TF-IDF and Cosine Similarity.

## Dataset
Custom movies dataset with 50 movies - title, genre, overview columns.

## How it works
1. Text from genre and overview is cleaned and vectorized using TF-IDF
2. Cosine similarity is computed between all movies
3. When you select a movie, top 5 most similar movies are returned

## Files
- `app.py` - Streamlit web app
- `movies.csv` - dataset
- `Assignment20_Shiza.ipynb` - notebook with all tasks
- `requirements.txt` - dependencies

## Run locally
```
pip install -r requirements.txt
streamlit run app.py
```

## Deployed App
[Link will be added after Render deployment]
