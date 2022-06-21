import sqlite3 as sql

con = sql.connect("db.sqlite3")
cur = con.cursor()
statement = "SELECT phone, alternatePhone, name FROM testsite_re_user"
cur.execute(statement)
print(cur.fetchall())
