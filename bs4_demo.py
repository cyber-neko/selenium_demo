import requests
from bs4 import BeautifulSoup

url = 'https://scraping-for-beginner.herokuapp.com/ranking'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

# 1つの観光地の情報を取得
spots = soup.find_all('div', attrs={'class': 'u_areaListRankingBox row'})
spot = spots[0]
spot_name = spot.find('div', attrs={'class': 'u_title'})
spot_name.find('span', attrs={'class': 'badge'}).extract()
spot_name = spot_name.text.replace('\n', '')
print(spot_name)
# 評点
eval_num = float(spot.find('div', attrs={'class': 'u_rankBox'}).text)
print(eval_num)

categoryItems = spot.find('div', attrs={'class': 'u_categoryTipsItem'})
categoryItems = categoryItems.find_all('dl')
# 楽しさのみ取得
categoryItem = categoryItems[0]
category = categoryItem.dt.text
print(categoryItem)
print(category)
rank = float(categoryItem.span.text)
print(rank)

# 連想配列に格納
details = {}

for categoryItem in categoryItems:
    category = categoryItem.dt.text
    rank = float(categoryItem.span.text)
    details[category] = rank

datum = details
datum['観光地名'] = spot_name
datum['評点'] = eval_num
print(datum)


# 全ての観光地を取得
soup = BeautifulSoup(res.text, 'html.parser')

data = []

spots = soup.find_all('div', attrs={'class': 'u_areaListRankingBox row'})
for spot in spots:
    spot_name = spot.find('div', attrs={'class': 'u_title'})

    spot_name.find('span', attrs={'class': 'badge'}).extract()
    spot_name = spot_name.text.replace('\n', '')
    eval_num = float(spot.find('div', attrs={'class': 'u_rankBox'}).text)

    categoryItems = spot.find('div', attrs={'class': 'u_categoryTipsItem'})
    categoryItems = categoryItems.find_all('dl')

    details = {}

    for categoryItem in categoryItems:
        category = categoryItem.dt.text
        rank = float(categoryItem.span.text)
        details[category] = rank

    datum = details
    datum['観光地名'] = spot_name
    datum['評点'] = eval_num
    data.append(datum)

print(data)


# csvへ抽出
import pandas as pd

df = pd.DataFrame(data)
print(df.columns)
df = df[['観光地名', '評点', '楽しさ', '人混みの多さ', '景色', 'アクセス']]
print(df.columns)

df.to_csv('観光地情報.csv', index=False)