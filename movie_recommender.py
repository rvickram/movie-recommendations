import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Helper functions
def get_title_from_index(data, index):
	return data[data.index == index]["title"].values[0]

def get_index_from_title(data, title):
	return data[data.title == title]["index"].values[0]
##################################################

## Read CSV file
df = movieData = pd.read_csv('./data/movie_dataset.csv')
print(df.head())

## Select features
features = ['keywords', 'cast', 'genres', 'director']
# combined the features into a single string
def combine_features(row):
	return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
df['combined_features'] = df.apply(combine_features, axis=1) # axis=1 means pass rows not columns
print(df['combined_features'].head())