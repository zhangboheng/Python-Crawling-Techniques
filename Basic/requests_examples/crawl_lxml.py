from lxml import html
import requests

response = requests.get('https://www.google.com')
tree = html.fromstring(response.content)
title = tree.xpath('//title/text()')[0]
print(title)
