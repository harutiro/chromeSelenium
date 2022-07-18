from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

browser = webdriver.Chrome()
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')

# ログイン画面
elem_username = browser.find_element(By.ID,'username')
elem_username.send_keys('imanishi')

elem_password = browser.find_element(By.ID,'password')
elem_password.send_keys('kohei')

sleep(1)
elem_login_btn = browser.find_element(By.ID,'login-btn')
elem_login_btn.click()

# 情報の取得
elem = browser.find_element(By.ID,'name')
name = elem.text

elem = browser.find_element(By.ID,'company')
company = elem.text

elem = browser.find_element(By.ID,'birthday')
birthday = elem.text

elem = browser.find_element(By.ID,'come_from')
come_from = elem.text

elem = browser.find_element(By.ID,'hobby')
hobby = elem.text
hobby = hobby.replace('\n',',')

# for分で情報を取得する
elem_th = browser.find_elements(By.TAG_NAME,'th')
keys = []
for elem in elem_th:
    print(elem.text)
    key = elem.text
    keys.append(key)

elem_td = browser.find_elements(By.TAG_NAME,'td')
values = []
for elem in elem_td:
    print(elem.text)
    value = elem.text
    values.append(value)

# ｃｓｖ出力をやってみる
df = pd.DataFrame()
df['項目'] = keys
df['値'] = values
print(df)
df.to_csv("講師情報.csv",index=False)


print("hello")