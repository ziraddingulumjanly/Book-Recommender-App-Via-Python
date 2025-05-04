import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess data
@st.cache_data
def load_data():
    books = pd.read_csv("recCSVs/Books.csv").drop(columns=['Image-URL-S', 'Image-URL-M'])
    ratings = pd.read_csv("recCSVs/Ratings.csv")

    # Filter out ratings <= 2
    ratings = ratings[ratings['Book-Rating'] > 2]

    # Keep only popular books
    book_counts = ratings['ISBN'].value_counts()
    ratings = ratings[ratings['ISBN'].isin(book_counts[book_counts >= 10].index)]

    # Keep only active users
    user_counts = ratings['User-ID'].value_counts()
    ratings = ratings[ratings['User-ID'].isin(user_counts[user_counts >= 5].index)]

    # Merge
    merged = ratings.merge(books, on='ISBN')

    # Create user-item matrix
    user_item_matrix = merged.pivot_table(index='User-ID', columns='Book-Title', values='Book-Rating')

    # Cosine similarity
    sim_matrix = cosine_similarity(user_item_matrix.T.fillna(0))
    similarity_df = pd.DataFrame(sim_matrix, index=user_item_matrix.columns, columns=user_item_matrix.columns)

    return books, similarity_df

# Load once
books_df, similarity_df = load_data()

# App UI
st.title("📚 Book Recommender System")
book_list = sorted(similarity_df.columns)
selected_book = st.selectbox("Choose a book you like:", book_list)

if st.button("Recommend"):
    if selected_book not in similarity_df.columns:
        st.error("Book not found.")
    else:
        recommendations = similarity_df[selected_book].dropna().sort_values(ascending=False)[1:11]
        recommended_titles = recommendations.index.tolist()

        # Get metadata and merge with similarity scores
        # Filter rows that match recommended titles
        details_raw = books_df[books_df['Book-Title'].isin(recommended_titles)]

        # Drop duplicate titles to keep only one row per book
        details = details_raw.drop_duplicates(subset=['Book-Title'])[
            ['Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Image-URL-L']
        ]

        # Ensure correct order and alignment with similarity scores
        details = details.set_index('Book-Title').loc[recommended_titles].reset_index()
        details['Similarity Score'] = recommendations.values.round(4)


        st.subheader("📖 Top 10 Similar Books:")

        # Table view
        st.dataframe(details[['Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Similarity Score']])

        # Image cards
        st.subheader("🖼️ Covers:")
        for _, row in details.iterrows():
            st.markdown(f"### {row['Book-Title']}")
            st.image(row['Image-URL-L'], width=150)
            st.caption(f"Author: {row['Book-Author']}  \nPublisher: {row['Publisher']}  \nYear: {row['Year-Of-Publication']}  \nSimilarity Score: {row['Similarity Score']}")
