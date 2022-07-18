from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')
sleep(4)


elem_username = browser.find_element(By.ID,'username')
elem_username.send_keys('imanishi')

elem_password = browser.find_element(By.ID,'password')
elem_password.send_keys('kohei')

sleep(1)
elem_login_btn = browser.find_element(By.ID,'login-btn')
elem_login_btn.click()
