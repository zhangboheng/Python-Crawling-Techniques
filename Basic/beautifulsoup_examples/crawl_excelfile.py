import xlwt
from xlwt import Workbook
from bs4 import BeautifulSoup
import requests

wb=Workbook()
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0,0,"Title")
sheet1.write(0,1,"Link")
sheet1.write(0,2,"Contents")

url = "https://www.luckydesigner.space"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
arr = []
for i in list(soup.select("h2>a")):
    arr.append(i.get_text())
lst = []
for i in list(soup.select("h2>a")):
    lst.append(i.get("href"))

cat = []
for i in lst:
    ret = requests.get(i)
    sup = BeautifulSoup(ret.text,"lxml")
    chi = [x.find_next("p").get_text() for x in sup.select("div>h4")[0:-1]]
    cat.append(chi)

i=1
while i<=len(lst):
    sheet1.write(i,1,"{}".format(lst[i-1]))
    sheet1.write(i,0,"{}".format(arr[i-1]))
    sheet1.write(i,2,"{}".format(cat[i-1]))
    i+=1

wb.save("demo.xls")