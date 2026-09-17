import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

st.set_page_config(
    page_title="Music Recommendation System",
    page_icon="🎵",
    layout="wide"
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

number_of_recommendations = st.selectbox(
    "Number of recommendations",
    [5, 10, 15]
)

def recommend(song_name, n_recommendations):
    index = song_indices[song_name]

    song_vector = X_scaled[index].reshape(1, -1)

    distances, indices = knn.kneighbors(
        song_vector,
        n_neighbors=n_recommendations + 1
    )

    recommendations = []

    for i in range(1, len(indices[0])):
        song_index = indices[0][i]

        recommendations.append({
            "Song": songs.iloc[song_index]["track_name"],
            "Artist": songs.iloc[song_index]["artists"],
            "Genre": songs.iloc[song_index]["track_genre"],
            "Similarity": round(1 - distances[0][i], 3)
        })

    return pd.DataFrame(recommendations)

st.sidebar.header("Genre Filter")

genres = ["All"] + sorted(
    songs["track_genre"].dropna().unique().tolist()
)

selected_genre = st.sidebar.selectbox(
    "Select Genre",
    genres
)

if st.button("Recommend Songs"):

    recommendations = recommend(
        selected_song,
        number_of_recommendations
    )

    if selected_genre != "All":
        recommendations = recommendations[
            recommendations["Genre"] == selected_genre
        ]

    st.subheader("Recommended Songs")

    st.dataframe(
        recommendations,
        use_container_width=True,
        hide_index=True
    )

    selected_data = songs[
        songs["track_name"] == selected_song
    ].iloc[0]

    st.subheader("Audio Characteristics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Danceability",
        round(selected_data["danceability"], 2)
    )

    col2.metric(
        "Energy",
        round(selected_data["energy"], 2)
    )

    col3.metric(
        "Valence",
        round(selected_data["valence"], 2)
    )

    col4.metric(
        "Tempo",
        round(selected_data["tempo"], 2)
    )

    chart_data = pd.DataFrame({
        "Feature": [
            "Danceability",
            "Energy",
            "Valence",
            "Tempo"
        ],
        "Value": [
            selected_data["danceability"],
            selected_data["energy"],
            selected_data["valence"],
            selected_data["tempo"]
        ]
    })

    st.subheader("Audio Characteristics Chart")

    fig = px.bar(
        chart_data,
        x="Feature",
        y="Value",
        title="Audio Characteristics"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    if len(recommendations) > 0:

        st.subheader("Recommendation Similarity")

        similarity_chart = recommendations.sort_values(
            "Similarity",
            ascending=True
        )

        fig2 = px.bar(
            similarity_chart,
            x="Similarity",
            y="Song",
            orientation="h",
            title="Similarity of Recommended Songs"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )
    else:
        st.warning("No songs found for the selected genre.")