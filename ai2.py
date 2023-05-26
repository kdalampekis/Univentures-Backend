# Import the necessary libraries
import sqlite3
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder


# Connect to the SQLite database
def connect_to_database():
    return sqlite3.connect('db.sqlite3')


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

    return event_ids, event_descriptions, event_categories, event_locations


# Fetch user's location from the database for the specified user
def fetch_user_location_from_database(cursor, user_id):
    cursor.execute("""
        SELECT main.uni_user.location
        FROM main.uni_user
        WHERE main.uni_user.id = ?
        """, (user_id,))
    user_location = cursor.fetchone()
    return user_location[0] if user_location else None


# Generate recommendations for the specified user
def generate_recommendations(user_id, cursor, N=2):
    user_preferences = fetch_user_preferences_from_database(cursor, user_id)
    event_ids, event_descriptions, event_categories, event_locations = fetch_event_data_from_database(cursor)

    # Fetch user's location from database
    user_location = fetch_user_location_from_database(cursor, user_id)

    # Step 3: Build Event-User Matrix
    matching_preferences = [pref for pref in user_preferences if pref in event_categories]

    if len(matching_preferences) == 0:
        print("No matching preferences found.")
        return []

    # Step 4: Apply TF-IDF Vectorization to Event Descriptions and Categories
    event_descriptions = [desc + ' ' + cat for desc, cat in zip(event_descriptions, event_categories)]
    tfidf_vectorizer = TfidfVectorizer()
    event_description_matrix = tfidf_vectorizer.fit_transform(event_descriptions)

    # Step 5: Incorporate Additional Event Features
    encoder = OneHotEncoder()
    event_location_matrix = encoder.fit_transform(np.array(event_locations).reshape(-1, 1))
    event_feature_matrix = np.hstack((event_description_matrix.toarray(), event_location_matrix.toarray()))

    # Create user_vector in the feature space
    user_descriptions = ' '.join(matching_preferences)
    user_description_matrix = tfidf_vectorizer.transform([user_descriptions])

    # Represent user's location in the encoded location space
    user_location_matrix = encoder.transform(np.array([user_location]).reshape(-1, 1)) if user_location else np.zeros((1, event_location_matrix.shape[1]))

    user_vector = np.hstack((user_description_matrix.toarray(), user_location_matrix.toarray()))

    # Step 6: Calculate Similarity Scores
    event_similarity_scores = cosine_similarity(user_vector, event_feature_matrix)[0]

    # Step 7: Generate User Recommendations
    top_n_events = np.argsort(event_similarity_scores)[::-1][:N]

    return [event_ids[i] for i in top_n_events]

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
