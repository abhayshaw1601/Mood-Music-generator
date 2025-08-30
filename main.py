import nltk
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from nltk.sentiment import SentimentIntensityAnalyzer
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os 

app = Flask(__name__)
CORS(app)

load_dotenv()

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)


def detect_mood(text):
    score = sia.polarity_scores(text)
    compound = score["compound"]

    if compound >= 0.6:
        return "very happy "
    elif 0.3 <= compound < 0.6:
        return "happy "
    elif 0.05 <= compound < 0.3:
        return "calm / relaxed "
    elif -0.05 < compound < 0.05:
        return "neutral "
    elif -0.3 <= compound <= -0.05:
        return "sad "
    elif -0.6 <= compound < -0.3:
        return "very sad "
    else:
        return "angry "


@app.route("/get_songs", methods=["POST"])     

def get_songs():
    data = request.get_json()
    user_text = data.get("message", "")
    platform = data.get("platform", "both")
    language = data.get("language", "random")

    mood = detect_mood(user_text)
    if language and language != "random":
        mood =f"{language} {mood}"

    result = sp.search(q=mood, type='track', limit=5)

    song = []

    for track in result['tracks']['items']:
        name = track['name']
        artist = track['artists'][0]['name']
        spotify_url = track['external_urls']['spotify']
        sname = name.replace(" ", "+")
        sname = sname.replace("'", "")
        sartist = artist.replace(" ", "+")
        sartist = sartist.replace("'", "")
        yt_query = f"https://www.youtube.com/results?search_query={sname}+{sartist}"

        song_entry = {"name": name, "artist": artist}
        if platform in ["both", "spot"]:
            song_entry["spotify"] = spotify_url
        if platform in ["both", "yt"]:
            song_entry["youtube"] = yt_query

        song.append(song_entry)

    return jsonify({"mood": mood, "songs": song})

if __name__ == "__main__":
    app.run(debug=True)
