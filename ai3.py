# Import the necessary libraries
import sqlite3
import sys
import numpy as np
import scipy.sparse as sp
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.decomposition import TruncatedSVD

# Connect to the SQLite database
def connect_to_database():
    return sqlite3.connect('/db.sqlite3')

# Fetch user preferences from the database for the specified user
def fetch_user_preferences_from_database(user_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT main.userpreferences.categories_id
        FROM userpreferences
        WHERE main.userpreferences.user_id = ?
        """, (user_id,))
    preferences_data = cursor.fetchall()
    user_preferences = []

    for preference in preferences_data:
        cursor.execute("""
            SELECT main.uni_categories.categ_name
            FROM uni_categories
            WHERE main.uni_categories.id = ?
            """, (preference[0],))
        category_name = cursor.fetchone()
        if category_name:
            user_preferences.append(category_name[0])

    cursor.close()
    conn.close()

    return user_preferences


# Fetch user ratings from the database for the specified user
def fetch_user_ratings_from_database(user_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT main.eventsuser.events_id, main.eventsuser.user_rating 
        FROM eventsuser 
        WHERE main.eventsuser.user_id=?
    """, (user_id,))
    ratings_data = cursor.fetchall()
    if ratings_data:
        user_ratings = {rating[0]: rating[1] for rating in ratings_data}
    else:
        user_ratings = {}

    cursor.close()
    conn.close()

    return user_ratings


# Fetch event data from the database
def fetch_event_data_from_database():
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT main.uni_events.id, description, location
        FROM uni_events
    """)
    event_data = cursor.fetchall()

    event_ids = []
    event_descriptions = []
    event_categories = []
    event_locations = []

    for event in event_data:
        event_ids.append(event[0])
        event_descriptions.append(event[1])
        event_locations.append(event[2])

        cursor.execute("""
            SELECT main.eventscategories.categories_id
            FROM eventscategories
            WHERE main.eventscategories.events_id = ?
        """, (event[0],))

        category_ids = cursor.fetchall()

        for category_id in category_ids:
            cursor.execute("""
                SELECT main.uni_categories.categ_name
                FROM uni_categories
                WHERE main.uni_categories.id = ?
            """, (category_id[0],))
            category_name = cursor.fetchone()
            if category_name:
                event_categories.append(category_name[0])

    cursor.close()
    conn.close()

    return event_ids, event_descriptions, event_categories, event_locations


# Generate recommendations for the specified user
def generate_recommendations(user_id, N=2):
    user_preferences = fetch_user_preferences_from_database(user_id)
    user_ratings = fetch_user_ratings_from_database(user_id)
    event_ids, event_descriptions, event_categories, event_locations = fetch_event_data_from_database()

    # Initialize user event ratings array
    event_user_ratings = np.ones(len(event_ids))  # Default to neutral rating

    # Update event ratings array based on user's past ratings
    for event_id in user_ratings.keys():
        if event_id in event_ids:
            event_index = event_ids.index(event_id)
            event_user_ratings[event_index] = user_ratings[event_id]

    # Apply TF-IDF Vectorization to Event Descriptions
    tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=2)
    event_description_matrix = tfidf_vectorizer.fit_transform(event_descriptions)

    # Incorporate Additional Event Features
    encoder = OneHotEncoder()
    event_category_matrix = encoder.fit_transform(np.array(event_categories).reshape(-1, 1))
    event_location_matrix = encoder.fit_transform(np.array(event_locations).reshape(-1, 1))
    event_feature_matrix = sp.hstack((event_description_matrix, event_category_matrix, event_location_matrix))

    # Reduce Dimensionality with Truncated SVD
    svd = TruncatedSVD(n_components=40)
    event_feature_matrix = svd.fit_transform(event_feature_matrix)

    # Calculate Similarity Scores
    event_similarity_matrix = linear_kernel(event_feature_matrix, event_feature_matrix)

    # Compute weighted event-user similarity score
    event_user_similarity = event_similarity_matrix.dot(event_user_ratings)

    # Normalize similarity scores
    scaler = MinMaxScaler()
    event_user_similarity = scaler.fit_transform(event_user_similarity.reshape(-1, 1)).flatten()

    # Get the top N event indices based on similarity scores
    top_n_event_indices = np.argsort(event_user_similarity)[::-1][:N]

    # Get the top N recommended event ids
    recommended_events = [event_ids[i] for i in top_n_event_indices]

    return recommended_events


# Entry point of the script
if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Get the user ID from the command-line argument
        user_id = sys.argv[1]
    else:
        # Prompt the user for the user ID
        user_id = input("Enter the User ID: ")

    # Assuming N is the number of recommendations to generate
    N = 2

    # Generate recommendations for the specified user
    recommended_events = generate_recommendations(user_id, N)

    # Display the recommended events
    if recommended_events:
        print(f"Recommended Events for User {user_id}:")
        for event_id in recommended_events:
            print(f"Event: {event_id}")
            print()
    else:
        print("No recommended events found.")
