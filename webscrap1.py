from bs4 import BeautifulSoup
import requests
import pandas as pd
url ='https://www.nfl.com/standings/league/2020/reg'
page=requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
print(soup)

table_data = soup.find('table',class_="d3-o-table d3-o-table--row-striping d3-o-table--detailed d3-o-standings--detailed d3-o-table--sortable {sortlist: [[4,1]], sortinitialorder: 'desc'}")

headers = []
for i in table_data.find_all('th'):
    title = i.text.strip()
    headers.append(title)

df = pd.DataFrame(columns = headers)
for row in table_data.find_all('tr')[1:]:
        row_data = row.find_all('td')
        row_1= [tr.text.strip() for tr in row_data]
        length = len(df)
        df.loc[length] = row_1
col=df.columns
print(col)
for i in col:
    for j in df[i]:
        print("original :{0},Datatype: {1}".format(j,type(j)))