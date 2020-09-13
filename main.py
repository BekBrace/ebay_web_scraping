'Ebay Website Scraping in Python '
import requests
from bs4 import BeautifulSoup
URL = 'https://www.ebay.com/p/26030651821?iid=313191277769'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 OPR/70.0.3728.178'}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

product_title = soup.find(class_='product-title').get_text()
product_price = soup.find(class_='display-price').get_text()
product_price_value = int(product_price[1:4])
# print(product_title)
# print(product_price_value)


def check_price():
    if(product_price_value < 300):
        print('Congrats! The price has fallen to : $', product_price_value)
    else:
        print('Sorry! The price is still $400')


if __name__ == "__main__":
    check_price()
