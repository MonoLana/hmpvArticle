# HMPV Article Title Analysis

## 📌 Project Overview

This project analyzes the sentiment of **HMPV (Human Metapneumovirus) article titles** over the years. The goal is to observe trends in sentiment and gain insights into how the perception of HMPV has evolved.

## 🛠 Technologies Used

- **Python**: Main programming language
- **NLTK (Natural Language Toolkit)**: Tokenization and text preprocessing
- **TextBlob**: Sentiment analysis
- **Matplotlib**: Data visualization

## 📂 Project Structure

```
hmpvArticle/
├── dataset/             # Contains raw and processed datasets
├── explore.ipynb        # Jupyter Notebooks for analysis
├── preprocessing.py     # Python scripts for processing and analysis
├── requirements.txt     # Dependancies documentation
├── README.md            # Project documentation
```

## 🔍 Sentiment Analysis Workflow

1. **Data Collection**: Gather article titles from kaggle.
2. **Preprocessing**: Tokenization, lowercasing, and stopword removal using NLTK.
3. **Sentiment Extraction**: Use TextBlob to classify titles into positive, negative, or neutral sentiments.
4. **Visualization**: Plot sentiment trends over the years using Matplotlib.

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/MonoLana/hmpvArticle.git
cd hmpvArticle
```

### 2️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

## 📌 Future Improvements

- Expanding the dataset with more sources
- Using advanced NLP models like VADER or transformers for sentiment analysis
- Adding interactive visualizations with Plotly or Streamlit
