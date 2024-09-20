import os
import time
import random
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs

ua = UserAgent()
header = {"User-Agent":ua.random}#伪装浏览器头部
proxies = [
    '45.43.71.88:6686',
    '142.111.1.252:5284',
    '173.244.41.45:6229',
    '142.147.131.197:6097',
    '156.239.55.100:3128',
    '107.181.141.250:6647',
    '104.238.49.180:5834',
    '104.165.169.240:3128',
    '45.141.83.163:6527',
]
ip=random.choice(proxies)
proxy_ip = 'http://' + ip
proxy_ips = 'https://' + ip
proxy = {'https': proxy_ips, 'http': proxy_ip} 
url = "https://avgle.com/videos?page={}"
lst = []
for page in range(1,11):
    time.sleep(2)
    soup = bs(requests.get(url.format(page), headers=header, proxies=proxy).text, "lxml")
    chat = soup.find_all("div", "well well-sm")
    link = list(x.find_next("a")["href"] for x in chat)
    for i in link:
        lst.append("https://www.avgle.com{}".format(i))
dir_name = "avlge"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
with open(dir_name+"/"+"avgleList.txt","w") as f:
    for a in sorted(list(set(lst)), key=lst.index):
        f.write(a+"\n")