import mysql.connector

a=mysql.connector.connect(host='localhost',user='root',passwd='root',database='dbase')
cursor=a.cursor()
cursor.execute('create table employee(id int ,name varchar(200),salary int,year int)')
a.close()