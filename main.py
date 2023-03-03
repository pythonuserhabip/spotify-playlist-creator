import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
client_id = "c8bf9a804f0f468eaa6241b33a884f6b"
client_secret = "927af1070ae74b8f8496c297e7eb1823"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]
song_uris = ["The list of", "song URIs", "you got by", "searching Spotify"]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, "html.parser")


songs_name = soup.select(selector="li h3", class_="c-title")
songs_list = []

for song in songs_name:
    text = song.getText().strip()
    songs_list.append(text)

print(songs_list)





sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= client_id,
        client_secret= client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)






