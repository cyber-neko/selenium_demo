import requests
from bs4 import BeautifulSoup

url = 'https://scraping-for-beginner.herokuapp.com/image'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

img_tag = soup.find('img')
img_tag['src']

root_url = 'https://scraping-for-beginner.herokuapp.com'
img_url = root_url + img_tag['src']




from PIL import Image
import io

# 画像を1つ取得
# contentでバイナリデータを取得、Image.open()で画像を表示
img = Image.open(io.BytesIO(requests.get(img_url).content))
img.save('img/sample.jpg')
# requests.get(img_url)


# 複数の画像を取得
soup = BeautifulSoup(res.text, 'html.parser')

img_tags = soup.find_all('img')

# enumerateでインデックスの値と要素を取り出す
for i, img_tag in enumerate(img_tags):
    root_url = 'https://scraping-for-beginner.herokuapp.com'
    img_url = root_url + img_tag['src']

    img = Image.open(io.BytesIO(requests.get(img_url).content))
    img.save(f'img/{i}.jpg')
