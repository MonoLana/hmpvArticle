import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
from textblob import TextBlob
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

stop_words = set(stopwords.words('english'))
medical_stop_words = {'study', 'analysis', 'review', 'case', 'patient', 'patients',
                         'results', 'using', 'based', 'associated', 'clinical'}
# using update to update the set from stopwords from custom medical stopwords
stop_words.update(medical_stop_words)

lemmatizer = WordNetLemmatizer()

df = pd.read_csv('dataset/articles.csv')
# convert the 'published' column to date format
df['published'] = pd.to_datetime(df['published'])
df['year_month'] = df['published'].dt.to_period('M')
df['year'] = df['published'].dt.year
df['month'] = df['published'].dt.month

# Clean the titles
def clean_title(title):
    if isinstance(title, str):  # Check if title is a string
        # Tokenize the title
        words = word_tokenize(title)
        # Remove stop words and non-alphabetic words, and lemmatize
        cleaned_words = [lemmatizer.lemmatize(word.lower()) for word in words if word.isalpha() and word.lower() not in stop_words]
        return ' '.join(cleaned_words)
    return ''  # Return empty string if title is not a string

def sentiment_labeling(
    text,
):  # label every row based on the polarity score with textblob
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    if score > 0:
        sentiment = "positive"
    elif score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return pd.Series([sentiment, score, subjectivity])



# Fill NaN values with empty strings
df['title'] = df['title'].fillna('')

# Apply the cleaning function to the titles
df['clean_text'] = df['title'].apply(clean_title)

'''
the apply() wont work if there is nan value in the list so you've to fill the nan value with empty string
'''

df[['sentiment', 'polarity', 'subjectivity']] = df['clean_text'].apply(sentiment_labeling)
print(df.head())

df.to_csv('dataset/result.csv')