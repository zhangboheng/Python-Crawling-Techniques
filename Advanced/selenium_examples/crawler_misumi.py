import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_categories(driver, selector):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
    )
    elements = driver.find_elements(By.CSS_SELECTOR, selector)
    categories = [(e.text, e.get_attribute('href')) for e in elements if e.text != '' and e.text != "经济型产品" and e.text != "非标AI报价" and e.text != "捆包用品/物流保管用品"]
    return categories

def navigate_and_extract(driver, url, selector):
    driver.get(url)
    return extract_categories(driver, selector)
s = Service('D:/Program Files/ChromeDriver/chromedriver.exe')
driver = webdriver.Chrome(service=s)

data = []

try:
    driver.get('https://www.misumi.com.cn/')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".l-header__logo"))
    )
    first_level = extract_categories(driver, "div.new-l-top__main ul li a")
    
    for title, link in first_level:
        print(f"First Level: {title}, {link}")
        data.append({'Level': 'First', 'Title': title, 'Link': link})
        second_level = navigate_and_extract(driver, link, "div.l-navCategoryBox ul li a")
        for title2, link2 in second_level:
            print(f"Second Level: {title2}, {link2}")
            data.append({'Level': 'Second', 'Title': title2, 'Link': link2})
            third_level = navigate_and_extract(driver, link2, "ul.lc-level4 li a")
            for title3, link3 in third_level:
                print(f"Third Level: {title3}, {link3}")
                data.append({'Level': 'Third', 'Title': title3, 'Link': link3})

finally:
    driver.quit()

df = pd.DataFrame(data)
df.to_excel('misumi_categories.xlsx', index=False)