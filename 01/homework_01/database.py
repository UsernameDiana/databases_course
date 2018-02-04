import sqlite3
import random
import time

conn = sqlite3.connect('database.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS digits ('
               'time REAL, num REAL)'
               )


def set_dynamic_data():
    t = time.time()
    num = random.randrange(0, 10)
    c.execute("INSERT INTO digits (time, num) VALUES (?, ?)",
               (t, num))
    conn.commit()


def read_db():
    c.execute('SELECT * FROM digits')
    for row in c.fetchall():
        print (row)


# create_table()
# for i in range(10):
#     set_dynamic_data()
#     time.sleep(1)
read_db()
c.close()
conn.close()
