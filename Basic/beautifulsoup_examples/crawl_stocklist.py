import requests
from bs4 import BeautifulSoup
import csv
import re

code = []
name = []
url = "http://quote.stockstar.com/stock/stock_index.htm"
req = requests.get(url)
req.encoding = "gb2312"
soup = BeautifulSoup(req.text, "html.parser")
for i in soup.find_all('ul', class_="seo_pageList"):
    for a in i.find_all('li'):
        sm = re.findall('\d+', a.text.strip())
        ms = a.text[6:]
        code.append(sm)
        name.append(ms)
with open("out.csv","w") as f:
    cr = csv.writer(f,delimiter=";",lineterminator="\n")
    cr.writerow(["股票代码","股票名称"])
    for i,j in zip(code,name):
        cr.writerow(["=\"" + i[0]+ "\"",j])
f.close()