from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.preprocessing import MinMaxScaler
from sklearn.externals import joblib
import implicit
import scipy.sparse as sp
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import GridSearchCV
import sqlite3

# Assuming you have an SQLite database file with appropriate tables for user data and event data
def fetch_user_data_from_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Fetch user preferences and ratings from the database
    user_preferences = {}
    user_ratings = {}

    # Execute SQL query to fetch user preferences
    cursor.execute("SELECT user_id, preferences FROM univ_user")
    preferences_data = cursor.fetchall()
    for user_id, preferences in preferences_data:
        user_preferences[user_id] = preferences.split(',')

    # Execute SQL query to fetch user ratings
    cursor.execute("SELECT user_id, event_id, rating FROM univ_user")
    ratings_data = cursor.fetchall()
    for user_id, event_id, rating in ratings_data:
        if user_id not in user_ratings:
            user_ratings[user_id] = {}
        user_ratings[user_id][event_id] = rating

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return user_preferences, user_ratings

def fetch_event_data_from_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Fetch event data from the database
    cursor.execute("SELECT event_id, event_name, description, location FROM univ_events")
    event_data = cursor.fetchall()

    event_ids = []
    event_descriptions = []
    event_categories = []
    event_locations = []

    for event in event_data:
        event_ids.append(event[0])
        event_descriptions.append(event[2])
        event_categories.append(event[1])
        event_locations.append(event[3])

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return event_ids, event_descriptions, event_categories, event_locations

def update_model():
    # Fetch user data from the SQLite database
    user_preferences, user_ratings = fetch_user_data_from_database()

    # Fetch event data from the SQLite database
    event_ids, event_descriptions, event_categories, event_locations = fetch_event_data_from_database()

    # Step 3: Build Event-User Matrix

    # Create a matrix with events as rows and users as columns
    event_user_matrix = [[user_ratings[user_id].get(event_id, 0)
                          for user_id in user_preferences.keys()]
                         for event_id in event_ids]

    # Step 4: Apply TF-IDF Vectorization to Event Descriptions

    tfidf_vectorizer = TfidfVectorizer()
    event_description_matrix = tfidf_vectorizer.fit_transform(event_descriptions)

    # Step 5: Incorporate Additional Event Features

    # Encode categorical event features
    encoder = OneHotEncoder()
    event_category_matrix = encoder.fit_transform(np.array(event_categories).reshape(-1, 1))
    event_location_matrix = encoder.fit_transform(np.array(event_locations).reshape(-1, 1))

    # Concatenate event description and additional feature matrices
    event_feature_matrix = sp.hstack((event_description_matrix, event_category_matrix, event_location_matrix))

    # Step 6: Calculate Similarity Scores

    # Calculate similarity scores between event descriptions and features
    event_similarity_matrix = linear_kernel(event_feature_matrix, event_feature_matrix)

    # Step 7: Generate User Recommendations

    recommendations = {}

    for user_id in user_preferences.keys():
        # Calculate the index of the current user in the user_preferences dictionary
        user_index = list(user_preferences.keys()).index(user_id)

        # Calculate similarity scores between the current user and events
        user_event_similarity = event_user_matrix.dot(event_similarity_matrix[user_index])

        # Scale the similarity scores to a range of [0, 1]
        scaler = MinMaxScaler()
        user_event_similarity = scaler.fit_transform(user_event_similarity.reshape(-1, 1)).flatten()

        # Sort the events based on similarity scores
        sorted_event_indices = sorted(range(len(user_event_similarity)), key=lambda k: user_event_similarity[k], reverse=True)

        # Get the top N recommended events
        top_n_events = [event_ids[idx] for idx in sorted_event_indices[:N]]

        recommendations[user_id] = top_n_events

    # Update the model with new data
    sparse_event_user_matrix = sp.csr_matrix(event_user_matrix)
    model = implicit.als.AlternatingLeastSquares(factors=50, regularization=0.01, iterations=20)
    model.fit(sparse_event_user_matrix)
    joblib.dump(model, 'trained_model.pkl')

    return recommendations

# Load the pre-trained model from disk (if available)
try:
    model = joblib.load('trained_model.pkl')
except FileNotFoundError:
    model = None

# Assuming N is the number of recommendations to generate
N = 2

while True:
    recommendations = update_model()

    # Display the recommended events for each user
    for user_id, top_n_events in recommendations.items():
        print(f"User: {user_id}")
        for event_id in top_n_events:
            print(f"Event: {event_id}")
        print()
