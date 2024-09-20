import requests
import re

def fetch_google_title():

    url = 'https://www.google.com'

    response = requests.get(url)

    if response.status_code == 200:
        title_match = re.search('<title>(.*?)</title>', response.text, re.IGNORECASE)
        
        if title_match:
            return title_match.group(1)
        else:
            return "Title not found"
    else:
        return "Failed to retrieve the webpage"

print(fetch_google_title())
