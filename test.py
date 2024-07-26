import sqlite3


con = sqlite3.Connection('dbs')
cur = con.cursor()
cur.execute("SELECT * FROM YesBook")
row = cur.fetchall()
print(row)