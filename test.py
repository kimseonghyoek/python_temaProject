import sqlite3


con = sqlite3.Connection('dbms')
cur = con.cursor()
cur.execute("SELECT * FROM YesBook")
row = cur.fetchall()
print(row)