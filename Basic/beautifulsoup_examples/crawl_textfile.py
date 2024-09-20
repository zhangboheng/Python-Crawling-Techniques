import requests
from bs4 import BeautifulSoup
url = "https://www.luckydesigner.space"
req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
f = open("demofile.txt", "w")
for i in soup.find_all("h2"):
    f.write("{}\n".format(i.string))
f.close()