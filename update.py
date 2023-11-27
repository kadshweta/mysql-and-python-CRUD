import mysql.connector

a=mysql.connector.connect(host='localhost',user='root',passwd='root',database='dbase')
cursor=a.cursor()

try:
    cursor.execute('update employee set name="prati" where id=2' )
    a.commit()
    print("record updated succefuly ")
except:
    a.rollback()


a.close()
