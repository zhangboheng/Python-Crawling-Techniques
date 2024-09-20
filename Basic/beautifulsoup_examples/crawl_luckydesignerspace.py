import requests
from bs4 import BeautifulSoup
url = "https://www.luckydesigner.space"
req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
for i in soup.find_all("h2"):
    print(i.string)