from dotenv import load_dotenv
from melon import *
from datetime import datetime
import json

# chart = ChartData()

# HTML 테이블 변환 함수
# def df_to_html():
#     html = '<table border="1" style="border-collapse: collapse; width: 80%; text-align: left;">'
#     html += "<tr><th>순위</th><th>아티스트</th><th>곡명</th><th>앨범 커버</th></tr>"
    
    
#     # print(song["rank"], song["artist"],song["title"], song["image"] )
#     for i in range(10):
#         song = json.loads(chart[i].json())
#         html += f'<tr><td>{song["rank"]}위</td><td>{song["artist"]}</td><td>{song["title"]}</td>'
#         html += f'<td><img src="{song["image"]}" width="100"></td></tr>'
#     html += "</table>"
#     return html



# HTML 파일 저장
# html_content = f"""
# <!DOCTYPE html>
# <html lang="ko">
# <head>
#     <meta charset="UTF-8">
# </head>
# <body>
#     <h2>음악 차트 TOP 10</h2>
#     <br>⏳ 업데이트 시간: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} (UTC)</br>
#     {df_to_html()}
# </body>
# </html>
# # """

# # 파일 저장
# with open("README.md", "w", encoding="utf-8") as f:
#     f.write(html_content)

# print("README.md 파일이 생성되었습니다.")
