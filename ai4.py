# Import the necessary libraries
import sqlite3
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
import scipy.sparse as sp


# Connect to the SQLite database
def connect_to_database():
    return sqlite3.connect('/db.sqlite3')


# Fetch user preferences from the database for the specified user
def fetch_user_preferences_from_database(cursor, user_id):
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

    return user_preferences


# Fetch event data from the database
def fetch_event_data_from_database(cursor):
    cursor.execute("""
        SELECT main.uni_events.id, description, location, main.uni_events.university_id
        FROM uni_events
    """)
    event_data = cursor.fetchall()

    event_ids = []
    event_descriptions = []
    event_categories = []
    event_locations = []
    event_university_id = []

    for event in event_data:
        event_ids.append(event[0])
        event_descriptions.append(event[1])
        event_locations.append(event[2])
        event_university_id.append(event[3])

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

    return event_ids, event_descriptions, event_categories, event_locations, event_university_id


# Fetch user's location from the database for the specified user
def fetch_user_location_from_database(cursor, user_id):
    cursor.execute("""
        SELECT main.uni_user.location
        FROM main.uni_user
        WHERE main.uni_user.id = ?
        """, (user_id,))
    user_location = cursor.fetchone()
    return user_location[0] if user_location else None


# Fetch user's university_id from the database for the specified user
def fetch_user_university_id_from_database(cursor, user_id):
    cursor.execute("""
        SELECT main.uni_user.university_id
        FROM main.uni_user
        WHERE main.uni_user.id = ?
        """, (user_id,))
    user_university_id = cursor.fetchone()
    return user_university_id[0] if user_university_id else None

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

# Generate recommendations for the specified user
# Generate recommendations for the specified user
def generate_recommendations(user_id, cursor, N=2):
    user_preferences = fetch_user_preferences_from_database(cursor, user_id)
    user_ratings = fetch_user_ratings_from_database(user_id)
    event_ids, event_descriptions, event_categories, event_locations, event_university_id = fetch_event_data_from_database(cursor)

    # Fetch user's location and university_id from database
    user_location = fetch_user_location_from_database(cursor, user_id)
    user_university_id = fetch_user_university_id_from_database(cursor, user_id)

    matching_preferences = [pref for pref in user_preferences if pref in event_categories]

    if len(matching_preferences) == 0:
        print("No matching preferences found.")
        return []

    event_descriptions = [desc + ' ' + cat for desc, cat in zip(event_descriptions, event_categories)]
    tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=2)
    event_description_matrix = tfidf_vectorizer.fit_transform(event_descriptions)

    location_encoder = OneHotEncoder()
    university_id_encoder = OneHotEncoder()
    category_encoder = OneHotEncoder()

    event_location_matrix = location_encoder.fit_transform(np.array(event_locations).reshape(-1, 1))
    event_university_matrix = university_id_encoder.fit_transform(np.array(event_university_id).reshape(-1, 1))
    event_category_matrix = category_encoder.fit_transform(np.array(event_categories).reshape(-1, 1))

    event_feature_matrix = sp.hstack(
        (event_description_matrix, event_category_matrix, event_location_matrix, event_university_matrix)).tocsr()

    # Create user_vector in the feature space
    user_descriptions = ' '.join(matching_preferences)
    user_description_matrix = tfidf_vectorizer.transform([user_descriptions])

    # Represent user's location in the encoded location space
    user_location_matrix = location_encoder.transform(
        np.array([user_location]).reshape(-1, 1)) if user_location else sp.csr_matrix((1, event_location_matrix.shape[1]))

    # Represent user's university in the encoded university space
    user_university_matrix = university_id_encoder.transform(
        np.array([user_university_id]).reshape(-1, 1)) if user_university_id else sp.csr_matrix((1, event_university_matrix.shape[1]))

    # Represent user's preferences in the encoded category space
    user_preferences_matrix = category_encoder.transform(
        np.array([user_preferences[0]]).reshape(-1, 1)) if user_preferences else sp.csr_matrix(
        (1, event_category_matrix.shape[1]))

    user_vector = sp.hstack((user_description_matrix, user_preferences_matrix, user_location_matrix, user_university_matrix)).tocsr()

    event_similarity_matrix = cosine_similarity(user_vector, event_feature_matrix)

    # Initialize user event ratings array
    event_user_ratings = np.ones(len(event_ids))  # Default to neutral rating

    # Update event ratings array based on user's past ratings
    for event_id in user_ratings.keys():
        if event_id in event_ids:
            event_index = event_ids.index(event_id)
            event_user_ratings[event_index] = user_ratings[event_id]

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
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Generate event recommendations for a user')
    parser.add_argument('user_id', help='The User ID to generate recommendations for')

    args = parser.parse_args()
    user_id = args.user_id

    conn = connect_to_database()
    cursor = conn.cursor()

    # Assuming N is the number of recommendations to generate
    N = 2

    # Generate recommendations for the specified user
    recommended_events = generate_recommendations(user_id, cursor, N)

    # Close the database connection
    cursor.close()
    conn.close()

    # Display the recommended events
    print(f"Recommended Events for User {user_id}:")
    for event_id in recommended_events:
        print(f"Event: {event_id}")
        print()
