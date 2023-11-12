import csv  
import sqlite3

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()

file = open('memberlist.csv')

contents = csv.reader(file)

insert_records = "INSERT INTO website_member ('first_name', 'last_name', 'institution', 'address', 'blood_group', 'payment_method', 'contact', 'date_of_birth', 'email') VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(insert_records, contents)

select_all = "SELECT * FROM website_member"
rows = cursor.execute(select_all).fetchall()

connection.commit()

connection.close()