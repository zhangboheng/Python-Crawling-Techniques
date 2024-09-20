from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('D:/Program Files/ChromeDriver/chromedriver.exe')

driver = webdriver.Chrome(service=service)

try:
    driver.get('https://www.google.com')

    title = driver.title
    print("The title of the page is:", title)

finally:
    driver.quit()
