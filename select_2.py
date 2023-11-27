import mysql.connector

a=mysql.connector.connect(host='localhost',user='root',passwd='root',database='dbase')
cursor=a.cursor()

try:
    cursor.execute('select * from employee order by id ')
    result=cursor.fetchall()
    for i in result:
        id = i[0]
        name=i[1]
        salary=i[2]
        year=i[3]
        print(id,name,salary,year)
except:
    print("some isuee in code ")

cursor.close()
