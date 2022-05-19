
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


# define a root `/` endpoint
@app.get("/")
def index():
    return {"Status": "Up and running"}


# Implement a /predict endpoint

@app.get("/predict")
def index(acousticness,
        danceability,
        duration_ms,
        energy,
        explicit,
        id,
        instrumentalness,
        key,
        liveness,
        loudness,
        mode,
        name,
        release_date,
        speechiness,
        tempo,
        valence,
        artist):

# creation X_test
    X_test=pd.DataFrame([[acousticness,
                danceability,
                duration_ms,
                energy,
                explicit,
                id,
                instrumentalness,
                key,
                liveness,
                loudness,
                mode,
                name,
                release_date,
                speechiness,
                tempo,
                valence,
                artist]],
                columns=['acousticness',
                        'danceability',
                        'duration_ms',
                        'energy',
                        'explicit',
                        'id',
                        'instrumentalness',
                        'key',
                        'liveness',
                        'loudness',
                        'mode',
                        'name',
                        'release_date',
                        'speechiness',
                        'tempo',
                        'valence',
                        'artist'])

    # load model from joblib
    model = joblib.load('assets/model.joblib')

    # definition y_pred
    y_pred = model.predict(X_test)

    return {"artist":artist,
            "name": name,
            "popularity": y_pred[0]
            }
