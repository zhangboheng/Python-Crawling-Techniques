import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
ua = UserAgent()
header = {"User-Agent": ua.random}
url = "https://free-proxy-list.net/"
req = requests.get(url, headers=header)
soup = bs(req.text, "html.parser")
proxies = []
for row in soup.find("table", attrs={"class": "table-striped"}).find_all("tr")[1:]:
    tds = row.find_all("td")
    try:
        ip = tds[0].text.strip()
        port = tds[1].text.strip()
        host = f"{ip}:{port}"
        proxies.append(host)
    except IndexError:
        continue
for i in proxies:
    print(i)