import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        cur = connection.cursor()
        cur.execute('''DELETE FROM products
                       WHERE id = 1;''')
        connection.commit()
        cur.close()
    except Error as e:
        print(f'The error "{e}" occurred.')
    return connection


con = create_connection('db.db')
