from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome import options

# 操作を一旦止める関数()内に秒数を入れる
sleep(3)
print('HERE')

# # ブラウザを起動、変数名はなんでも
# browser = webdriver.Chrome()
# # ブラウザを閉じる
# # browser.quit()

# url = 'https://scraping-for-beginner.herokuapp.com/login_page'
# browser.get(url)
# sleep(3)
# # 要素をid指定で探す
# elem_username =  browser.find_element_by_id('username')
# # send_keysでキーを送信できる
# elem_username.send_keys('imanishi')

# elem_password =  browser.find_element_by_id('password')
# elem_password.send_keys('kohei')
# elem_login_brn = browser.find_element_by_id('login-btn')
# # クリック操作
# sleep(1)
# elem_login_brn.click()
# browser.quit()



# ヘッドレスモード・・・GUIを返さずにCUIで処理を完結するモード
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)
browser.quit()