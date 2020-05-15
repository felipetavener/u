from bs4 import BeautifulSoup
import requests
import pandas as pd

link = 'https://www.selfridges.com/GB/en/cat/womens/on_sale'
page = requests.get(link).text
bs_page = BeautifulSoup(page, 'lxml')
# print(bs_page.text)
#print(bs_page.find('title').text)

#print(bs_page.find('div', class_='listing-items'))
#item_infos = bs_page.find('div', class_='listing-items')
#item_infos = bs_page.find_all('div', class_='richText-content')
# print(len(item_infos))
# for item in item_infos:
#     print(item)


prices = bs_page.find_all('div', class_='price-container')#.select('span', class_='now_price')
#print(len(prices))
#print(prices[0].text)
#print(prices[2].text)

was_price = []
now_price = []

for price in prices:
    p = price.select('span', class_='now_price')
    #print(len(p))
    was_price.append(p[2].text[1:])
    now_price.append(p[0].text[1:])

    '''
    if len(p) == 6:
        for elem in p:
            print(elem.text, end=' ')
        print()
    '''

#columns = ['Brand', 'Product', 'Was price', 'Now price','Discount']


was_price = list(map(float, was_price))
now_price = list(map(float, now_price))

discount = []

for was, now in zip(was_price, now_price):
    discounted = was-now
    discount.append(discounted)


data = {'Was price': was_price,
        'Now price': now_price,
        'Discount': discount
}


df = pd.DataFrame(data, columns = ['Was price', 'Now price', 'Discount'])

print(df.tail())
