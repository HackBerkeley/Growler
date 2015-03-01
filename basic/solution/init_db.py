import sqlite3
conn = sqlite3.connect('hakks.db')

c = conn.cursor()
c.execute("CREATE TABLE hakks (name, datetime, hakk)")
c.execute("INSERT INTO hakks VALUES ('richie', '100', 'Hello world!')")
c.execute("SELECT * FROM hakks")
print(c.fetchall())
conn.commit()
conn.close()
