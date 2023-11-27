import mysql.connector as msc 

a=msc.connect(
    host="localhost",
    user="root",
    password="root"
)

myc=a.cursor()
myc.execute("create database dbase")