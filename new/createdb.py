import mysql.connector
from tkinter import messagebox


def create_db():
    con=mysql.connector.connect(host='localhost',user='root',password='saagwe22',database="stock")
    cur=con.cursor()
   
    
    command="CREATE TABLE IF NOT EXISTS item (iid int auto_increment key not null,foodtype varchar(100),price varchar(100),location varchar(200),stock varchar(100),lastorder varchar(100))"
    cur.execute(command)

    


create_db()

