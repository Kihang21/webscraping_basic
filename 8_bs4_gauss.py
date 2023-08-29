import requests
from bs4 import BeautifulSoup

url = "https://www.dcinside.com"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
silbests = soup.find_all("div", attrs={"class":"box besttxt"})
# title = silbests[0].p.get_text()
# link = soup.select("a", ".main_log")
# print(title)
# print(link[0].text)

# 만화 제목 + 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "" + cartoon.a["href"]
#     print(title, link)

# 평점 구하기
