import mysql.connector

a=mysql.connector.connect(host='localhost',user='root',passwd='root',database='dbase')
cursor=a.cursor()
try:
    cursor.execute('insert into employee(id,name,salary,year) values(6,"niru",2700,2020)')
    a.commit()
    print("record are inserted successfully")
    # a.close()
except:
    a.rollback()

a.close()