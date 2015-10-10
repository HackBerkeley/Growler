import sqlite3
conn = sqlite3.connect('growls.db')

c = conn.cursor()
c.execute("delete from growls")
conn.commit()
conn.close()
