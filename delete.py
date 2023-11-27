import mysql.connector

a=mysql.connector.connect(host='localhost',user='root',passwd='root',database='dbase')
cursor=a.cursor()

try:
    cursor.execute('delete from employee where id=2 ')
    a.commit()
    print("data has been been delet successfully")
except:
    a.rollback()

a.close()