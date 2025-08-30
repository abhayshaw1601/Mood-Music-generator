---

## Mood-Music-Generator

A simple yet powerful app that recommends music based on your mood!
It analyzes your text input for sentiment, fetches mood-matching tracks from Spotify, and finds YouTube links for free playback.

---

### Features

* **Mood detection** using NLTK’s VADER sentiment analysis
* **Spotify integration** (via Spotipy) for dynamic music recommendations
* **YouTube fallback** using live search links
* **Optional language filtering**
* Compact, responsive **Flask-based web interface**
* Secure, environment-variable-driven API keys using a `.env` file

---

### Project Structure

```
Mood-Music-generator/
├── main.py
├── .env
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    ├── style.css
    ├── script.js
    └── send.png
```

---

### Installation & Setup

1. **Clone the repo:**

   ```bash
   git clone https://github.com/abhayshaw1601/Mood-Music-generator.git
   cd Mood-Music-generator
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your `.env` file:**
   Create a file named `.env` in the root folder with your Spotify credentials:

   ```
   SPOTIPY_CLIENT_ID=your_spotify_client_id_here
   SPOTIPY_CLIENT_SECRET=your_spotify_client_secret_here
   ```

---

### Running the App

Run the Flask server:

```bash
python main.py
```

Visit **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser to access the UI, input your mood, and get song recommendations.

---

### How It Works

1. **User input**: Type in a mood description.
2. **Sentiment analysis**: NLTK VADER determines if you're *happy*, *sad*, or *neutral*.
3. **Spotify search**: Fetches matching tracks programmatically.
4. **YouTube links**: Generates clickable links for free music playback.
5. **Language filter** (optional): Search is refined by adding the chosen language keyword.

---

### Customization Ideas

* Improve mood detection using advanced NLP (e.g., transformers)
* Add more mood categories (energetic, relaxed, etc.)
* Integrate with Spotify OAuth to **play music inside the app**
* Let users save their favorite songs (session-based playlists)
* Add UI enhancements like Dark Mode or a slider-based mood picker

---

### Contributions & Feedback

Contributions welcome!
Feel free to fork the project, make tweaks, and submit a pull request.
If you spot any bugs or have suggestions, open an issue—we’d love to hear from you.

---

### License

Licensed under the **MIT License**.

---
