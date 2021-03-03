from bs4 import BeautifulSoup
import requests

url = requests.get('https://www.jumia.co.ke/laptops/').text
soup = BeautifulSoup(url, 'lxml')
products = soup.find_all('article', class_='prd _fb col c-prd')

for product in products:
    prod_description = product.find('h3', class_='name').text
    current_price = product.find('div', class_='prc').text
    old_price = product.find('div', class_='old').text
    gap = product.find('div', class_='tag _dsct _sm').text
    rating = product.find('div', class_='stars _s').text

    print(f'''
    Product Description: {prod_description}
    Current Price: {current_price}
    Old Price: {old_price}
    Price gap: {gap}
    Rating: {rating}
    '''
          )
