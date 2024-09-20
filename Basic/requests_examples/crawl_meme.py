import requests
import urllib
from fake_useragent import UserAgent

ua = UserAgent()

#Fetch the available memes
data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]

#List all the memes
print('Here is the list of available memes : \n')
i = 1
for img in images:
    print(i,img['name'])
    i+=1

id = int(input('Enter the serial number of the meme : '))
text0 = input('Enter first text : ')
text1 = input('Enter second text : ')

URL = 'https://api.imgflip.com/caption_image'
# Resister your account on https://imgflip.com/ and get the username and password
params = {
    'username':"", #Enter your username
    'password':"", #Enter your password
    'template_id':images[id-1]['id'],
    'text0':text0,
    'text1':text1
}
response = requests.request('POST',URL,params=params).json()
abc = response["data"]["url"]
req = requests.get(abc)
with open("demo.jpg", "wb") as f:
    f.write(req.content)