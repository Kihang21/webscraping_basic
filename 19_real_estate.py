# [출력 결과]
# =========== 메믈 1 ===========
# 거래 : 매매
# 면적 : 84/59 (공급/전용)
# 가격 : 165,000 (만원)
# 동 : 214동
# 층 : 고/23
# =========== 매물 2 ===========
# ...

import requests
from bs4 import BeautifulSoup

url = "https://new.land.naver.com/complexes/111515?ms=37.497624,127.107268,17&a=APT:PRE&e=RETAIL&articleNo=2330632137"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

with open("quiz.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())
