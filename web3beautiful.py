import requests
from bs4 import BeautifulSoup

res = requests.get('https://scraping-for-beginner.herokuapp.com/udemy')
print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

# 情報の取得
subscribers = soup.find_all('p',attrs={'class':'subscribers'})[0]
n_subscribers = int(subscribers.text.split('：')[1])
print(n_subscribers)

reviews = soup.find_all('p',attrs={'class':'reviews'})[0]
n_reviews = int(reviews.text.split('：')[1])
print(n_reviews)

# ｃｓｓセレクタ
print(soup.select('.subscribers'))
print(soup.select_one('.reviews').text)