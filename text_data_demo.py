from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')

elem_username = browser.find_element_by_id('username')
elem_username.send_keys('imanishi')
elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')
elem_login_btn = browser.find_element_by_id('login-btn')
elem_login_btn.click()

elem = browser.find_element_by_id('name')
# テキストを取得する
print(elem.text)

elem = browser.find_element_by_id('company')
print(elem.text)
elem = browser.find_element_by_id('birthday')
print(elem.text)
elem = browser.find_element_by_id('come_from')
print(elem.text)
elem = browser.find_element_by_id('hobby')
print(elem.text)

#　複数取得する場合はelementsであることに注意
elems_th = browser.find_elements_by_tag_name('th')
print(elems_th[0].text)

keys = []
for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)

elems_td = browser.find_elements_by_tag_name('td')
values = []
for elem_td in elems_td:
    value = elem_td.text
    values.append(value)

print(keys)
print(values)

import pandas as pd
df = pd.DataFrame()

df['項目'] = keys
df['値'] = values

# csvに出力、index=Falseでインデックスを消去
df.to_csv('講師情報.csv', index=False)

# browser.quit()