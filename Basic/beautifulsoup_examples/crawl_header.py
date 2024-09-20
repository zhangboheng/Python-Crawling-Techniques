from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
ua = UserAgent()
url = "https://movie.douban.com"
headers = {"User-Agent":ua.random}
req = requests.get(url,headers=headers)
soup = BeautifulSoup(req.text, "html.parser")
for i in soup.select("li.title"):
    print(i.get_text().replace("\n",""))