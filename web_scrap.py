from bs4 import BeautifulSoup
import requests

link = 'https://www.selfridges.com/GB/en/cat/womens/on_sale'
page = requests.get(link).text
bs_page = BeautifulSoup(page, 'lxml')

# print(bs_page.find('div', class_='listing-items'))
print(bs_page.find('div', class_='component-content'))
#item_infos = bs_page.find('div', class_='listing-items')
#item_infos = bs_page.find_all('div', class_='richText-content').select('a', class_='href')

# item_infos = bs_page.find_all('a')
# for item in item_infos:
#         print(item.get('href'))

# item_infos = bs_page.select('a', href=True, text=True)
#
# for item in item_infos:
#         print(item.prettify())
