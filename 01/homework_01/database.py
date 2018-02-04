import sqlite3
import random
import string

conn = sqlite3.connect('database.db')
c = conn.cursor()


def create_table():
    c.execute(
        'CREATE TABLE IF NOT EXISTS symbols (letters TEXT, numbers REAL)'
    )


def set_dynamic_data():
    char = string.ascii_letters
    t = ''.join(random.sample(char, 5))
    num = random.randrange(0, 10)
    c.execute(
        "INSERT INTO symbols (letters, numbers) VALUES (?, ?)", (t, num)
    )
    conn.commit()


def read_db():
    c.execute('SELECT * FROM symbols')
    for row in c.fetchall():
        print (row)


# create_table()
# for i in range(10):
#     set_dynamic_data()
read_db()
c.close()
conn.close()
