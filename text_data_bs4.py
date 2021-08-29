import requests
from bs4 import BeautifulSoup

url = 'https://scraping-for-beginner.herokuapp.com/udemy'
res = requests.get(url)

# html.parserとはHTMLの構造を解析すること
soup = BeautifulSoup(res.text, 'html.parser')
# prettify()フォーマットをきれいにする関数
print(soup.prettify())
# soup.find_all('要素名') attrs={'class': 'クラス名'}でクラスを指定、配列でとってくるので[0]で中身を取り出す
subscribers = soup.find_all('p', attrs={'class': 'subscribers'})[0]
print(subscribers.text)
#　数字の部分のみを取得する
n_subscribers = int(subscribers.text.split('：')[1])
print(n_subscribers)

reviews = soup.find_all('p', attrs={'class': 'reviews'})[0]
print(reviews.text)
n_reviews = int(reviews.text.split('：')[1])
print(n_reviews)