from lib2to3.pgen2.pgen import DFAState
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go
import seaborn as sns
import warnings
warnings.filterwarnings('always')
warnings.filterwarnings('ignore')
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import flask
from flask import Flask, redirect, render_template, request, url_for
import pickle

app = Flask(__name__)

# Define tfidf_matrix globally
tfidf_matrix = None

# Load the updated dataset
zomato_df = pd.read_csv('restaurant1.csv')


def get_recommendations(user_query):
    # Convert to lowercase
    user_query = user_query.lower()

    # Tokenize words
    keywords = user_query.split()

    # Match restaurants where any keyword appears in cuisine or name
    zomato_df['match_score'] = zomato_df.apply(
        lambda row: sum(kw in row['cuisines'].lower() or kw in row['name'].lower() for kw in keywords), axis=1
    )

    # Optional: Also apply a cost filter if keywords include 'cheap', 'budget', etc.
    if 'cheap' in keywords or 'budget' in keywords or 'low' in keywords:
        zomato_df_filtered = zomato_df[zomato_df['cost'] <= 500]
    else:
        zomato_df_filtered = zomato_df

    # Filter and sort by match and rating
    results = zomato_df_filtered[zomato_df_filtered['match_score'] > 0]
    results = results.sort_values(by=['match_score', 'Mean Rating'], ascending=[False, False])

    if results.empty:
        return "Sorry, no matching restaurants found. Try different keywords!"
    
    return results[['name', 'cuisines', 'Mean Rating', 'cost']].head(10)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommend():
    return render_template('recommend.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        restaurant_name = request.form.get('restaurant_name')
        if not restaurant_name:
            return "Error: No restaurant name provided. Please go back and enter a restaurant name."
        top_restaurants = get_recommendations(restaurant_name)
        if isinstance(top_restaurants, str):
            # If top_restaurants is a string, it's an error message
            return top_restaurants
        top_restaurants_list = top_restaurants.to_dict('records')
        return render_template('result.html', recommended_restaurants=top_restaurants_list)
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)




