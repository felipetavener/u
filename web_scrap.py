from bs4 import BeautifulSoup
import requests

link = 'https://www.selfridges.com/GB/en/cat/womens/on_sale'
page = requests.get(link).text
bs_page = BeautifulSoup(page, 'lxml')
# print(bs_page.text)
#print(bs_page.find('title').text)

#print(bs_page.find('div', class_='listing-items'))
#item_infos = bs_page.find('div', class_='listing-items')
#item_infos = bs_page.find_all('div', class_='richText-content').select('a', class_='href')

item_infos = bs_page.find_all('a')


for item in item_infos:
        print(item.get('href'))

# item_infos = bs_page.select('a', href=True, text=True)
#
# for item in item_infos:
#         print(item.prettify())



prices = bs_page.find_all('div', class_='price-container')#.select('span', class_='now_price')

#print(len(prices))
#print(prices[0].text)
#print(prices[2].text)
# for price in prices:
#     p = price.select('span', class_='now_price')
#     #print(len(p))
#     print(p[0].text, p[2].text)

'''
    if len(p) == 6:
        for elem in p:
            print(elem.text, end=' ')
        print()
'''

