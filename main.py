# библиотека для отправки/получения запросов на сервер 
import requests

# библиотека для работы с форматом json (десириализации полученого запроса)
import json

# библиотека для создания запросов sql при помощи PYTHON
import sqlite3


def myFunc(urlPage):
    myRiquest = requests.get(r'https://swapi.dev/api/people/?page=' + urlPage)
    if myRiquest.status_code == 200:
        objFromString = json.loads(myRiquest.text)
        resultKey = objFromString['results']
        for j in range(len(resultKey)):

            myList = [ resultKey[j]['name'], resultKey[j]['height'], resultKey[j]['eye_color'], resultKey[j]['gender'] ]
            try:
                myConection.commit()
                myCursor.execute('INSERT INTO Сharacters(name, height, eye_color, gender) VALUES(?,?,?,?);',myList)
                myConection.commit()
            except:
                myConection.rollback()

            myList.clear()



myConection = sqlite3.connect('starWorsDataBase.db')
myCursor = myConection.cursor()
myCursor.executescript('''
DROP TABLE IF EXISTS "Сharacters";
CREATE TABLE "Сharacters" (
    "id"    INTEGER PRIMARY KEY AUTOINCREMENT,
    "name"    TEXT UNIQUE,
    "height"  INTEGER,
    "eye_color" TEXT,
    "gender" TEXT
    );
''')

for i in range(1, 10):
    myFunc(str(i))

# myCursor.execute('SELECT * FROM Сharacters WHERE eye_color == "blue";')
# print(myCursor.fetchall())

# myCursor.execute('SELECT * FROM Сharacters ORDER BY height DESC;')
# print(myCursor.fetchmany(3))

# myCursor.execute("SELECT * FROM Сharacters WHERE height > 170 AND gender LIKE '%male%'; ")
# print(myCursor.fetchall())

myCursor.close()