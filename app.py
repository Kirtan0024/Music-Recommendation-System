import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Music Recommendation System",
    page_icon="🎵"
)

songs = pickle.load(open("models/songs.pkl", "rb"))
knn = pickle.load(open("models/knn.pkl", "rb"))
X_scaled = pickle.load(open("models/X_scaled.pkl", "rb"))
song_indices = pickle.load(open("models/song_indices.pkl", "rb"))

st.title("🎵 Music Recommendation System")
st.write("Find songs similar to your favorite track.")

song_list = songs["track_name"].dropna().unique()

selected_song = st.selectbox(
    "Select a song",
    song_list
)

def recommend(song_name):
    index = song_indices[song_name]

    song_vector = X_scaled[index].reshape(1, -1)

    distances, indices = knn.kneighbors(
        song_vector,
        n_neighbors=11
    )

    recommendations = []

    for i in range(1, len(indices[0])):
        song_index = indices[0][i]

        recommendations.append({
            "track_name": songs.iloc[song_index]["track_name"],
            "artists": songs.iloc[song_index]["artists"],
            "track_genre": songs.iloc[song_index]["track_genre"],
            "similarity": round(1 - distances[0][i], 3)
        })

    return pd.DataFrame(recommendations)

if st.button("Recommend Songs"):
    recommendations = recommend(selected_song)

    st.subheader("Recommended Songs")

    for _, row in recommendations.iterrows():
        st.write(
            f"🎵 {row['track_name']} — {row['artists']}"
        )
        st.caption(
            f"Genre: {row['track_genre']} | Similarity: {row['similarity']}"
        )