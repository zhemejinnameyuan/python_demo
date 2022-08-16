import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()
cur.execute('''
CREATE TABLE face ( 
name TEXT NOT NULL,
encoding TEXT NOT NULL)
''')