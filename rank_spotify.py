import os
import requests
import base64

# Spotify API 키 불러오기
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Spotify API 토큰 요청
def get_spotify_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    }
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, data=data)
    return response.json().get("access_token")

# Spotify API에서 인기 플레이리스트 가져오기
def get_top_songs():
    token = get_spotify_token()
    url = "https://api.spotify.com/v1/browse/featured-playlists"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
        
    playlists = response.json().get("playlists", {}).get("items", [])
    top_songs = []
    
    for playlist in playlists[:5]:  # 상위 5개만 가져오기
        name = playlist["name"]
        url = playlist["external_urls"]["spotify"]
        top_songs.append(f"- [{name}]({url})")
    
    return top_songs

# 결과를 Markdown 파일로 저장
def save_to_readme():
    songs = get_top_songs()
    with open("top_songs.md", "w", encoding="utf-8") as f:
        f.write("### 🎵 인기 있는 Spotify 플레이리스트\n\n")
        f.write("\n".join(songs))
        f.write("\n\n_Last updated: " + requests.get("https://worldtimeapi.org/api/timezone/Etc/UTC").json()["datetime"] + "_")

# 실행
if __name__ == "__main__":
    save_to_readme()
