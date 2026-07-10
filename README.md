# 🎬 Movie Recommendation System

**Assignment 20 — GenAI Course**
**Name:** Shiza

---

## 📌 About
A **Content-Based Movie Recommendation System** built using **TF-IDF Vectorization** and **Cosine Similarity**. Given a movie, the system recommends the top 5 most similar movies based on genre and overview text.

---

## 🗂️ Dataset
- Custom dataset: `movies.csv`
- Contains **50 movies** with the following columns:
  - `title` — Movie name
  - `genre` — Genre(s) of the movie
  - `overview` — Short description/plot

---

## ⚙️ How It Works

1. **Text Preprocessing** — Genre and overview combined, lowercased, punctuation removed, stopwords filtered
2. **TF-IDF Vectorization** — Text converted into numerical vectors (`max_features=500`, `ngram_range=(1,2)`)
3. **Cosine Similarity** — Similarity matrix computed between all movie vectors
4. **Recommendation** — Top 5 most similar movies returned for selected movie

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas | Data loading & manipulation |
| Scikit-learn | TF-IDF + Cosine Similarity |
| NLTK | Stopwords removal |
| Streamlit | Web app UI |

---

## 📁 Files

| File | Description |
|------|-------------|
| `app.py` | Streamlit web application |
| `movies.csv` | Movie dataset (50 movies) |
| `Assignment20_Shiza.ipynb` | Jupyter notebook with all tasks & analysis |
| `requirements.txt` | Python dependencies |

---

## 🚀 Run Locally

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the app
streamlit run app.py
```

App will open at: `http://localhost:8501`

---

## 🌐 Deployed App

> 🔗 [Link will be added after deployment]

---

## 📸 How to Use

1. Select a movie from the dropdown
2. Click **"Get Recommendations"**
3. Get top 5 similar movie suggestions instantly!
