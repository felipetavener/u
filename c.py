from bs4 import BeautifulSoup
import requests
import pandas as pd

link = 'https://www.worldometers.info/coronavirus/'
page = requests.get(link).text
page = page.replace("<br />", " ").replace("&nbsp;", "")
f = open('c.html', 'w', encoding='utf-8')
f.write(page)
f.close()
bs_page = BeautifulSoup(page, 'lxml')

table = bs_page.find('table', {'id': 'main_table_countries_today'}).find_all('tr')
header = []
for row in table[0].find_all('th'):
    header.append(row.text)
print(header)

body = [] #['USA', '1,469,972, +12,379 87,706  +794 317,477 1,064,789 16,173 4,444 265 10,780,662 32,594 330,753,490']
for row in table[9:-8]:
    r = []
    for cell in row.find_all('td'):
        r.append(cell.text)
    body.append(r)


df = pd.DataFrame(body, columns = header)




# 1) remove +, ,
# 2) convert to Integer


header_numbers = ['Total Cases', 'New Cases', 'Total Deaths',
       'New Deaths', 'Total Recovered', 'Active Cases', 'Serious, Critical',
       'TotCases/ 1M pop', 'Deaths/ 1M pop', 'Total Tests',
       'Tests/ \n1M pop\n', 'Population']