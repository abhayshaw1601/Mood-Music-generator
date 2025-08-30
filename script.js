document.addEventListener("DOMContentLoaded", () => {
  const userInput = document.getElementById("moodInput");
  const platformSelect = document.getElementById("link-select");
  const languageSelect = document.getElementById("language-select");
  const sendBtn = document.getElementById("sendButton");
  const responseArea = document.getElementById("responseArea");
  const toggleBtn = document.getElementById("themeToggle");

  const API_URL = "http://127.0.0.1:5000/get_songs"; 

  const message =async () => {
    const moodText = userInput.value.trim();
    const platform = platformSelect.value;
    const language = languageSelect.value;

    if (!moodText) {
      alert("Please enter mood.");
      return;
    }
    if (!platform) {
      alert("Please select a platform.");
      return;
    }
    if (!language) {
      alert("Please select a language.");
      return;
    }

    responseArea.innerHTML = "<p>Loading...</p>";

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: moodText, platform,language })
      });

      const data = await response.json();
      // responseArea.innerHTML = `<h3>Detected mood: ${data.mood}</h3>`;

      data.songs.forEach(song => {
        let songHTML = `<p>${song.name} - ${song.artist}`;
        if (song.spotify) songHTML += ` | <a href="${song.spotify}" target="_blank">Spotify</a>`;
        if (song.youtube) songHTML += ` | <a href="${song.youtube}" target="_blank">YouTube</a>`;
        songHTML += "</p>";
        responseArea.innerHTML += songHTML;
      });
    } catch (error) {
      console.error("Error:", error);
      responseArea.innerHTML = "<p>Something went wrong. Try again later.</p>";
    }
  } ;

  sendBtn.addEventListener("click", async () => {
    message();
  });

  userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      message();
    }
  });


  toggleBtn.addEventListener("click", () => {
    document.body.classList.toggle("dark");
    toggleBtn.textContent = document.body.classList.contains("dark") ? "☀️" : "🌙";
  });
});
