import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
init2 = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(init2)
cursor.execute("INSERT INTO users VALUES(null, ?, ?)", ("Gautam", "WOW"))
print("Users Table Created...")
init = "CREATE TABLE IF NOT EXISTS cars (name text, make text, power int)"
cursor.execute(init)
print("Cars Table Created...")
car = ("488_GTB", "FERRARI", 500)
insert = "INSERT INTO cars VALUES (?, ?, ?)"
cursor.execute(insert, car)
car = ("F12", "FERRARI", 700)
insert = "INSERT INTO cars VALUES (?, ?, ?)"
cursor.execute(insert, car)
result = cursor.execute("SELECT * FROM cars")
alls = result.fetchall()
print(alls)
init_d = "CREATE TABLE IF NOT EXISTS drivers (name text, team text, rating real)"
cursor.execute(init_d)
driver = ("VETTEL", "FERRARI", 5)
insert = "INSERT INTO drivers VALUES (?, ?, ?)"
cursor.execute(insert, driver)
result = cursor.execute("SELECT * FROM drivers")
alls = result.fetchall()
print(alls)
connection.commit()
connection.close()

