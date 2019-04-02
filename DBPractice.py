import sqlite3
#sqllite 설치해야 함

#DB 연결, 커서 생성
conn = sqlite3.connect('DB파일 위치')
cursor = conn.cursor()

#Insert
cursor.execute("insert sql문")
id = cursor.lastrowid
print(id)
cursor.execute("insert sql문")
id = cursor.lastrowid
print(id)

conn.commit()

#select
cursor.execute("select ~")
rows = cursor.fetchall()
for r in rows :
    print("sql문")

#delete, update 모두 insert와 동일한 과정

#DB, 커서 해제
cursor.close()
conn.close()
