# Spotify_API

The goal of this project is to create an API that will predict the popularity of a song based on its other features.
The API returns a json, here is an exemple :
{
  "artist": "John Hartford",
  "name": "Back in the Goodle Days",
  "popularity": 22
}

A trained model is saved as assets/model.joblib.
The code of the API is available in api/fast.py

### Install the required packages
pip install -r requirements.txt

### Run a uvicorn server
uvicorn api.fast:app --reload

Open browser : http://localhost:8000/

### Exemple request :
http://127.0.0.1:8000/predict?acousticness=0.654&danceability=0.499&duration_ms=219827&energy=0.19&explicit=0&id=0B6BeEUd6UwFlbsHMQKjob&instrumentalness=0.00409&key=7&liveness=0.0898&loudness=-16.435&mode=1&name=Back%20in%20the%20Goodle%20Days&release_date=1971&speechiness=0.0454&tempo=149.46&valence=0.43&artist=John%20Hartford

### Run the directives of the Makefile and then Cloud run !
