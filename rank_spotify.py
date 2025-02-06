import os
import requests
import base64
from dotenv import load_dotenv
import datetime
from melon import *
import json

chart = ChartData()

# df = pd.DataFrame(chart)
# print(df.head(10))

# HTML 테이블 변환 함수
def df_to_html():
    html = '<table border="1" style="border-collapse: collapse; width: 80%; text-align: left;">'
    html += "<tr><th>순위</th><th>아티스트</th><th>곡명</th><th>앨범 커버</th></tr>"
    
    
    # print(song["rank"], song["artist"],song["title"], song["image"] )
    for i in range(10):
        song = json.loads(chart[i].json())
        html += f'<tr><td>{song["rank"]}위</td><td>{song["artist"]}</td><td>{song["title"]}</td>'
        html += f'<td><img src="{song["image"]}" width="100"></td></tr>'
    html += "</table>"
    return html

# HTML 파일 저장
html_content = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>음악 차트</title>
</head>
<body>
    <h2>음악 차트 TOP 10</h2>
    {df_to_html()}
</body>
</html>
"""

# 파일 저장
with open("readme.md", "w", encoding="utf-8") as f:
    f.write(html_content)

print("readme.md 파일이 생성되었습니다.")
# df = pd.DataFrame(chart)
# print(df.head(10))
# df = pd.DataFrame(chart)
# print(df.head(10))

# load_dotenv()
# # Spotify API 키 불러오기
# CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
# CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# # Spotify API 토큰 요청
# def get_spotify_token():
#     url = "https://accounts.spotify.com/api/token"
#     headers = {
#     "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
#     "Content-Type": "application/x-www-form-urlencoded"
# }
#     data = {"grant_type": "client_credentials"}
#     response = requests.post(url, headers=headers, data=data)
#     return response.json().get("access_token")

# # Spotify API에서 인기 플레이리스트 가져오기
# def get_top_songs():
#     token = get_spotify_token()
#     url = "https://api.spotify.com/v1/browse/featured-playlists"
#     headers = {"Authorization": f"Bearer {token}"}
#     response = requests.get(url, headers=headers)

#     playlists = response.json().get("playlists", {}).get("items", [])
#     top_songs = []
    
#     for playlist in playlists[:5]:  # 상위 5개만 가져오기
#         name = playlist["name"]
#         url = playlist["external_urls"]["spotify"]
#         top_songs.append(f"- [{name}]({url})")
    
#     return top_songs

# # 결과를 Markdown 파일로 저장
# def save_to_readme():    
#     now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     songs = get_top_songs()
#     with open("top_songs.md", "w", encoding="utf-8") as f:
#         f.write("### 🎵 인기 있는 Spotify 플레이리스트\n\n")
#         f.write("\n".join(songs))
#         f.write("\n\n_Last updated: "+ now+"(UTC)")

# # 실행
# if __name__ == "__main__":
#     save_to_readme()
