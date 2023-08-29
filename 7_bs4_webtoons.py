import requests
from bs4 import BeautifulSoup

url = "https://www.dcinside.com"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
silbests = soup.find_all("p")
for silbests in silbests:
    print(silbests.get_text())