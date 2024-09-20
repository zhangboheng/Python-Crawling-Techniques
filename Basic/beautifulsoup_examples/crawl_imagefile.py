import os
import re
import time
import requests
from bs4 import BeautifulSoup

url = "https://www.luckydesigner.space"
req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
images = soup.find_all("img")
lst = []
for i in images:
    lst.append(i.attrs["src"])
dir_name = "iwate"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
for img in lst:
    time.sleep(2)
    picture_name = re.findall("\w.+[jpg]", img.split('/')[-1])[0]
    reponse = requests.get(img)
    with open(dir_name+'/'+picture_name,'wb') as f:
        f.write(reponse.content)