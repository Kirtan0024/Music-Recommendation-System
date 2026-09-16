Music Recommendation System

Overview

Music Recommendation System is a machine learning project that recommends songs based on their audio characteristics and similarity to a selected song.

The system uses Spotify music data containing features such as danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, and other song information.

The recommendation system calculates the similarity between songs using their numerical audio features and returns songs that are most similar to the selected track.

Features
Song-based music recommendations
Select a song and get similar songs
Adjustable number of recommendations
Displays song name, artist, genre, and similarity
Uses audio characteristics for recommendation
Interactive Streamlit web application
Exploratory Data Analysis
Feature scaling
Cosine similarity for finding similar songs
Technologies Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Streamlit
Jupyter Notebook
Git
GitHub
Dataset

The project uses a music dataset containing information about songs and their audio characteristics.

Important features used in the recommendation system include:

Danceability
Energy
Loudness
Speechiness
Acousticness
Instrumentalness
Liveness
Valence
Tempo

The raw dataset is not included in this repository if its size or license makes redistribution inappropriate.

How It Works

The recommendation system follows these steps:

Load the music dataset.
Clean and prepare the data.
Perform exploratory data analysis.
Select relevant audio features.
Scale the numerical features.
Calculate cosine similarity between songs.
Find songs similar to the selected song.
Display the recommendations through a Streamlit application.
Project Structure
Music-Recommendation-System/
│
├── data/
│   └── songs.csv
│
├── notebooks/
│   └── music_recommendation.ipynb
│
├── models/
│   ├── similarity.pkl
│   └── songs.pkl
│
├── screenshots/
│   ├── eda.png
│   ├── recommendation.png
│   └── dashboard.png
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
Installation

Clone the repository:

git clone https://github.com/Kirtan0024/Music-Recommendation-System.git

Move into the project directory:

cd Music-Recommendation-System

Install the required libraries:

pip install -r requirements.txt
Run the Application

Run the Streamlit application using:

streamlit run app.py

The application will open in your web browser.

Recommendation Method

The system uses cosine similarity to compare songs based on their selected audio features.

Songs with higher similarity values are considered more similar according to the features used by the recommendation model.


Future Improvements
Add genre-based filtering
Add personalized user recommendations
Add more interactive visualizations
Improve recommendation accuracy
Add playlist generation
Deploy the application online

How to Run
1. Clone the Repository
git clone https://github.com/Kirtan0024/Music-Recommendation-System.git
2. Open the Project Folder
cd Music-Recommendation-System
3. Install Required Libraries
pip install -r requirements.txt
4. Run the Streamlit Application
streamlit run app.py
5. Open the Application

After running the command, Streamlit will provide a local URL such as:
http://localhost:8501
Open this URL in your browser.

Author

Kirtan Parmar
GitHub: https://github.com/Kirtan0024