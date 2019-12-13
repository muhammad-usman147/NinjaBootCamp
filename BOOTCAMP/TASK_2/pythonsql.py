import sqlite3 as sq

conn = sq.connect("UsmanDataBase.db")
#creating database file with the name UsmanDataBase

c = conn.cursor()
'''
c.execute(""" CREATE TABLE employee (
    first text,
    last text,
    pay integer
    ) """)
conn.commit()
'''
c.execute("INSERT INTO employee VALUES('shakeel','ahmed','14241')")
conn.commit()

c.execute("SELECT * FROM employee ")
print(c.fetchall())
conn.commit()
conn.close()