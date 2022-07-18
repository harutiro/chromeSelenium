import sqlite3

dbname = 'TEST.db'
conn = sqlite3.connect(dbname)
# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

# personsというtableを作成してみる
# 大文字部はSQL文。小文字でも問題ない。
# cur.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT , name STRING)')

# "name"に"Taro"を入れる
cur.execute('INSERT INTO persons(name) values("Taro")')
# 同様に
cur.execute('INSERT INTO persons(name) values("Hanako")')
cur.execute('INSERT INTO persons(name) values("Hiroki")')

# terminalで実行したSQL文と同じようにexecute()に書く
cur.execute('SELECT * FROM persons')

# 中身を全て取得するfetchall()を使って、printする。
print(cur.fetchall())

cur.execute('SELECT * FROM persons')
print(type(cur.fetchall()))

cur.execute('SELECT * FROM persons')
print(len(cur.fetchall()))

cur.execute('SELECT * FROM persons')
index = 0
for i in cur.fetchall():
    index += 1

print(index)

# データベースへコミット。これで変更が反映される。
conn.commit()
conn.close()