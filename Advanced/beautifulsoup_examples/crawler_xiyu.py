import requests
from bs4 import BeautifulSoup
import chardet
import pandas as pd

url = 'https://www.ehsy.com/index.php?route=home/category/ajax_category_sub_tree'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

response = requests.get(url, headers=headers)

detected_encoding = chardet.detect(response.content)['encoding']

response.encoding = detected_encoding
soup = BeautifulSoup(response.content, 'html.parser')

categories = []

for li in soup.find_all('li', class_='tree-sub-li'):
    category_name = li.find('span', class_='tree-sub-li-left').a.text.strip()
    sub_categories = []
    for sub in li.find_all('span', class_='li-right-title'):
        sub_name = sub.a.text.strip()
        sub_url = sub.a['href']
        sub_categories.append({'Subcategory Name': sub_name, 'URL': sub_url})
    
    categories.append({'Category Name': category_name, 'Subcategories': sub_categories})

rows = []
for category in categories:
    for sub in category['Subcategories']:
        rows.append({
            'Category Name': category['Category Name'],
            'Subcategory Name': sub['Subcategory Name'],
            'URL': sub['URL']
        })


def fetch_product_details(url):
    response = requests.get(url, headers=headers)
    response.encoding = chardet.detect(response.content)['encoding']
    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = []
    
    product_list = soup.find_all('div', class_='product')
    for product in product_list:
        image = product.select('.image-div img')[0]['src']
        name = product.find('div', class_='p-name').text.strip()
        brand = product.find('li', class_='high-light').text.strip()
        price = product.find('span', class_='yen').text.strip()
        
        products.append({
            'Image URL': image,
            'Product Name': name,
            'Brand': brand,
            'Price': price
        })
        
    return products

all_products = []

for category in categories:
    for sub in category['Subcategories']:
        print(f"Fetching products for: {sub['Subcategory Name']} at {sub['URL']}")
        products = fetch_product_details(sub['URL'])
        for product in products:
            all_products.append({
                'Category Name': category['Category Name'],
                'Subcategory Name': sub['Subcategory Name'],
                'Product Name': product['Product Name'],
                'Brand': product['Brand'],
                'Price': product['Price'],
                'Image URL': product['Image URL'],
                'Product URL': sub['URL']
            })

df_products = pd.DataFrame(all_products)
df_products.to_excel('product_details.xlsx', index=False)