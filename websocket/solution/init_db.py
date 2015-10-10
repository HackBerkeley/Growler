import sqlite3
conn = sqlite3.connect('growls.db')

c = conn.cursor()
c.execute("CREATE TABLE growls (name, datetime, growl)")
c.execute("INSERT INTO growls VALUES ('richie', '100', 'Hello world!')")
c.execute("SELECT * FROM growls")
print(c.fetchall())
#c.execute("delete from growls")
conn.commit()
conn.close()
