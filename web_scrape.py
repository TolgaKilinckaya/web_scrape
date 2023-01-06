import requests
import csv
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')

book_containers = soup.find_all('article', class_ ='product_pod')

for container in book_containers:
    title = container.h3.a.text
    price = container.find('div', class_ = 'product_price').p.text
    print(title, price)

with open('books_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    
    writer.writerow(['title', 'price'])

    for container in book_containers:
        title = container.h3.a.text
        price = container.find('div', class_ = 'product_price').p.text
        writer.writerow([title, price])
