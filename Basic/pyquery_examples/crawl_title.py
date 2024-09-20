from pyquery import PyQuery as pq

d = pq(url='https://www.google.com')
title = d('title').text()
print(title)
