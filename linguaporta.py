from re import T
from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlite3
from time import sleep

# ログイン関係
print("ログインしています...")
print("IDを入力してください。")
id = input()
print("パスワードを入力してください。")
pw = input()

print("問題を選択したらEnterを押してください。終わる時はendを入力してください。")


browser = webdriver.Chrome()
browser.get('https://ait1.linguaporta.jp/user/ait/index.php')
sleep(2)

# IDとパスワードを入力
elem_id = browser.find_element(By.NAME,'id')
elem_id.send_keys(id)

elem_password = browser.find_element(By.NAME,'password')
elem_password.send_keys(pw)

#  問題のところに移動する
sleep(1)
elem_login_btn = browser.find_element(By.ID,'btn-login')
browser.execute_script('arguments[0].click();', elem_login_btn)

elem_login_btn = browser.find_element(By.CLASS_NAME,'btn.btn-menu.menu-study')
browser.execute_script('arguments[0].click();', elem_login_btn)

elem_login_btn = browser.find_element(By.CLASS_NAME,'btn.btn-reference-select')
browser.execute_script('arguments[0].click();', elem_login_btn)

while True:
    # 問題選択待ち
    inputStr = input()
    if inputStr == "end":
        try:
            conn.commit()
            conn.close()
        except:
            print("DB接続エラー")
        break

    # 問題確認
    elem_title = browser.find_element(By.CLASS_NAME,'bloc-resp.bloc-resp-lessonname')
    print(elem_title.text)

    title_number = elem_title.text.split(' ')[0]
    title_content = elem_title.text.split(' ')[1]
    tableName = ""

    flag = 0

    if title_content == '多肢選択':
        tableName = f'Q{title_number}1'
        flag = 1
    elif title_content == '単一選択':
        tableName = f'Q{title_number}2'
        flag = 2
    elif title_content == '記述問題':
        tableName = f'Q{title_number}3'
        flag = 3
    elif title_content == '記述問題':
        tableName = f'Q{title_number}4'
        flag = 4

    # DB
    dbname = 'linguaporta.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    try:
        cur.execute(f'CREATE TABLE {tableName}(question INTEGER PRIMARY KEY , ans STRING)')
    except:
        print("もう既にDBは作られています。")

    values = []
    questions = []

    # ラジオボタン形式
    while flag == 1:
        sleep(1)

        elem_question = browser.find_element(By.XPATH,'//*[@id="question_td"]/form[1]/b')
        question_ = int(elem_question.text.split('：')[1])
        cur.execute(f'select * from {tableName} where question == {question_};')
        print(cur.fetchall())   
        
        cur.execute(f'select * from {tableName} where question == {question_};')
        if len(cur.fetchall())==0:
            elem_radio_0 = browser.find_element(By.ID,'answer_0_0')
            elem_radio_0.click()

            elem_push = browser.find_element(By.ID,'ans_submit')
            elem_push.click()

            sleep(1)
            try:
                sleep(1)
                elem_ans_btn = browser.find_element(By.XPATH,'//input[@value=\'正解を見る\']')
                browser.execute_script('arguments[0].click();', elem_ans_btn)
            except:
                print("no answer")

            elem_ans = browser.find_element(By.ID,'drill_form')
            value = elem_ans.text.split('：')[1].split('\n')[0].replace('○','')
            values.append(value)

            elem_question = browser.find_element(By.XPATH,'//*[@id="question_td"]/form[1]/b')
            question = int(elem_question.text.split('：')[1])
            questions.append(question)

            # print(type(question))
            # print(type(value))

            cur.execute(f'INSERT INTO {tableName}(question , ans) values( {question} , \'{value}\' )')

            # print(values)
            # print(questions)
            # 中身を全て取得するfetchall()を使って、printする。
            cur.execute(f'SELECT * FROM {tableName}')
            print(cur.fetchall())   
        else:
            elem_radio_0 = browser.find_element(By.ID,'answer_0_0')
            elem_label_0 = browser.find_element(By.XPATH,'//*[@id="drill_form"]/label[1]')
            elem_radio_1 = browser.find_element(By.ID,'answer_0_1')
            elem_label_1 = browser.find_element(By.XPATH,'//*[@id="drill_form"]/label[2]')
            elem_radio_2 = browser.find_element(By.ID,'answer_0_2')
            elem_label_2 = browser.find_element(By.XPATH,'//*[@id="drill_form"]/label[3]')
            elem_radio_3 = browser.find_element(By.ID,'answer_0_3')
            elem_label_3 = browser.find_element(By.XPATH,'//*[@id="drill_form"]/label[4]')

            cur.execute(f'select * from {tableName} where question == {question_};')
            ansCheck = cur.fetchall()[0][1]

            if elem_label_0.text == ansCheck:
                browser.execute_script('arguments[0].click();', elem_radio_0)

            elif elem_label_1.text == ansCheck:
                browser.execute_script('arguments[0].click();', elem_radio_1)

            elif elem_label_2.text == ansCheck:
                browser.execute_script('arguments[0].click();', elem_radio_2)

            elif elem_label_3.text == ansCheck:
                browser.execute_script('arguments[0].click();', elem_radio_3)

            elem_push = browser.find_element(By.ID,'ans_submit')
            elem_push.click()

        
        try:
            sleep(1)
            elem_next_btn = browser.find_element(By.XPATH,'//input[@value=\'次の問題へ\']')
            browser.execute_script('arguments[0].click();', elem_next_btn)
            conn.commit()
        except:
            print("end")
            print("==========================================================")
            print("問題を選択したらEnterを押してください。終わる時はendを入力してください。")
            flag = 0
            break
    




# elem_login_btn = browser.find_element(By.XPATH,'//*[@id="content-study"]/div[1]/div[3]/div[1]/div/input')
# elem_login_btn.click()
