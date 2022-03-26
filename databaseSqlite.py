import sqlite3

conn = sqlite3.connect('customers.db')

c = conn.cursor()


c.execute("SELECT * FROM customer ORDER BY email ")
print(c.fetchall())




#commit our command
conn.commit()

conn.close()
