from tkinter import *
from tkinter import messagebox
import ast
import tkinter as tk
from tkinter import ttk,messagebox
from datetime import *

from PIL import Image, ImageTk
import subprocess

from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
from tkinter import messagebox
import subprocess


root=Tk()
root.title('Login')
root.geometry('925x400+300+200')
root.configure(bg="#b4c7e7")
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()

    if username=="admin" and password=="12345":
        root.withdraw()
        class DataClass:
            def __init__(self,window):
                self.window=window
                self.window.geometry("1100x500+220+130")
                self.window.title ("Add Data")                                                                    
                self.window.config(bg="black")
                self.window.focus_force()
                
                
                #icon image
                icon_image=PhotoImage(file="Images/login icon.png")
                window.iconphoto(False,icon_image)
                
                self.Data_photo1=Image.open("Images/Layer 3.png")
                self.Data_photo1=ImageTk.PhotoImage(self.Data_photo1)
                Label(window,image=self.Data_photo1,background="#000").place(x=50,y=5)
                
                
                
                #=======================================
                #All Variables===================



                self.var_item_id=StringVar()
                self.var_food_type=StringVar()
                self.var_stock=StringVar()
                self.var_price=StringVar()
                self.var_lastorder=StringVar()
                
            

                #=====searchFrame=====
                

                #====title=====
                title=Label(self.window,text="Add Stock",font=("arial",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)

                #======Content======
                #===row1========
                lbl_empid=Label(self.window,text="Item ID",font=("arial",15),bg="black",fg="white").place(x=50,y=150)
                txt_empid=Entry(self.window,textvariable=self.var_item_id,font=("arial",15)).place(x=150,y=150,width=180)
            

                #===row2========
                lbl_foodtype=Label(self.window,text="Food type",font=("arial",15),bg="black",fg="white").place(x=50,y=190)
                txt_foodtype=Entry(self.window,textvariable=self.var_food_type,font=("arial",15)).place(x=150,y=190,width=180)
                
                
                lbl_dob=Label(self.window,text="Stock",font=("arial",15),bg="black",fg="white").place(x=350,y=190)
                txt_dob=Entry(self.window,textvariable=self.var_stock,font=("arial",15)).place(x=500,y=190,width=180)
                

                #===row3========
                lbl_price=Label(self.window,text="Price",font=("arial",15),bg="black",fg="white").place(x=50,y=230)
                txt_price=Entry(self.window,textvariable=self.var_price,font=("arial",15)).place(x=150,y=230,width=180)

                
                lbl_pass=Label(self.window,text="Last Order",font=("arial",15),bg="black",fg="white").place(x=350,y=230)
                txt_pass=Entry(self.window,textvariable=self.var_lastorder,font=("arial",15)).place(x=500,y=230,width=180)
            

                #===row4========
                lbl_address=Label(self.window,text="Location",font=("arial",15),bg="black",fg="white").place(x=50,y=270)
            
                self.txt_location=Text(self.window,font=("arial",15))
                self.txt_location.place(x=150,y=270,width=300,height=60)
            
            
            #==============button============
                
                btn_add=Button(self.window,text="Add",command=self.add,font=("arial",15),cursor="hand2").place(x=500,y=305,width=110,height=28)
                btn_update=Button(self.window,text="Update",command=self.update,font=("arial",15),cursor="hand2").place(x=620,y=305,width=110,height=28)
                btn_delete=Button(self.window,text="Delete",command=self.delete,font=("arial",15),cursor="hand2").place(x=740,y=305,width=110,height=28)
                btn_clear=Button(self.window,text="Clear",command=self.clear,font=("arial",15),cursor="hand2").place(x=860,y=305,width=110,height=28)
                self.im1=Image.open("Images/logout.png")
                # self.im1=self.im1.resize((500,250),Image.ANTIALIAS)
                self.im1=ImageTk.PhotoImage(self.im1)
                btn_logout=Button(self.window,image=self.im1,font=("arial",15),bg="#607d8b",fg="white",cursor="hand2",command=self.logout).place(x=1000,y=40)

            #================Data Details==========
                frame=Frame(self.window,bd=3,relief=RIDGE)
                frame.place(x=0,y=350,relwidth=1,height=150)

                scrolly=Scrollbar(frame,orient=VERTICAL)
                scrollx=Scrollbar(frame,orient=HORIZONTAL)
                

                self.StockTable=ttk.Treeview(frame,columns=("iid","foodtype","price","location","stock","lastorder"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)
                scrollx.config(command=self.StockTable.xview)
                scrolly.config(command=self.StockTable.yview)
                self.StockTable.heading("iid",text="Item ID")
                self.StockTable.heading("foodtype",text="Food Type")
                self.StockTable.heading("price",text="Price")
                self.StockTable.heading("location",text="Location")
                self.StockTable.heading("stock",text="Stock")
                self.StockTable.heading("lastorder",text="Last Order")
                self.StockTable["show"]="headings"

                self.StockTable.column("iid",width=60)
                self.StockTable.column("foodtype",width=110)
                self.StockTable.column("price",width=140)
                self.StockTable.column("location",width=60)
                self.StockTable.column("stock",width=100)
                self.StockTable.column("lastorder",width=80)
                
                self.StockTable.pack(fill=BOTH,expand=1)
                self.StockTable.bind("<ButtonRelease-1>",self.get_data)

                self.show()
                
                
                
            def logout(self):
                
                    try:
                        window.destroy()
                        root.deiconify()
                    except subprocess.CalledProcessError as e:
                            print(f"Error running") 
        #=====================================================================================================================
            def add(self):
                con=mysql.connector.connect(host='localhost',user='root',password='saagwe22',database="stock")
                cur=con.cursor()
            
                cur.execute("Insert into item (iid,foodtype,price,location,stock,lastorder) values(%s,%s,%s,%s,%s,%s)",(
                                    self.var_item_id.get(),
                                            
                                    self.var_food_type.get(),
                                    self.var_price.get(),
                                    self.txt_location.get('1.0',END),
                                    
                                    self.var_stock.get(),
                                    
                                    self.var_lastorder.get(),
                                    
                                    


                    ))
                con.commit()
                messagebox.showinfo("Success","Data Added Successfully",parent=self.window)
                self.show()




            def show(self):
                con=mysql.connector.connect(host='localhost',user='root',password='saagwe22',database="stock")
                cur=con.cursor()
                try:
                    cur.execute("select * from item")
                    rows=cur.fetchall()
                    self.StockTable.delete(*self.StockTable.get_children())
                    for row in rows:
                        self.StockTable.insert('',END,values=row)

                except Exception as ex:
                    messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.window)
                    

            def get_data(self,ev):
                f=self.StockTable.focus()
                content=(self.StockTable.item(f))
                row=content['values']
                #print(row) 
                self.var_item_id.set(row[0])     
                self.var_food_type.set(row[1])
                self.var_price.set(row[2])  
                self.txt_location.delete('1.0',END)
                self.txt_location.insert(END,row[3])                             
                self.var_stock.set(row[4])            
                self.var_lastorder.set(row[5])



            def update(self):
                con=mysql.connector.connect(host='localhost',user='root',password='saagwe22',database="stock")
                cur=con.cursor()
                try:
                    if self.var_item_id.get()=="":
                        messagebox.showerror("Error","Data ID Must be required",parent=self.window)
                    else:
                        cur.execute("Select * from item where iid=%s",(self.var_item_id.get(),))
                        row=cur.fetchone()
                        if row==None:
                            messagebox.showerror("Error","Invalid Data ID",parent=self.window)
                        else:
                            cur.execute("Update item set foodtype=%s,price=%s,location=%s,stock=%s,lastorder=%s where iid=%s",(
                                                    
                                                self.var_food_type.get(),
                                                self.var_price.get(),
                                                self.txt_location.get('1.0',END),
                                        
                                                self.var_stock.get(),
                                                self.var_lastorder.get(),
                                                self.var_item_id.get()
                            

                                                    
                                                


                            ))
                            con.commit()
                            messagebox.showinfo("Success","Data Updated Successfully",parent=self.window)
                            self.show()


                except Exception as ex:
                    messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.window)

            def delete(self):
                con=mysql.connector.connect(host='localhost',user='root',password='saagwe22',database="stock")
                cur=con.cursor()
                try:
                    if self.var_item_id.get()=="":
                        messagebox.showerror("Error","item ID Must be required",parent=self.window)
                    else:
                        cur.execute("Select * from item where iid=%s",(self.var_item_id.get(),))
                        row=cur.fetchone()
                        if row==None:
                            messagebox.showerror("Error","Invalid item ID",parent=self.window)
                        else:
                            op=messagebox.askyesno("Confirm","Do you really want to delete%s",parent=self.window)
                            if op==True:
                                cur.execute("delete from item where iid=%s",(self.var_item_id.get(),))
                                con.commit()
                                messagebox.showinfo("Delete","item  Deleted Successfully",parent=self.window)
                                self.clear()
                    
                except Exception as ex:
                    messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.window)

            def clear(self):
                self.var_item_id.set("")     
                self.var_food_type.set("")
                self.var_price.set("")                          
                self.var_stock.set("")            
                
                self.var_lastorder.set("")
                self.txt_location.delete('1.0',END)

                self.show()
            
            
                    


        if __name__=="__main__":
            window=Toplevel(root)
            obj=DataClass(window)
            window.mainloop()   
    else:
        messagebox.showerror("error","Invalid id !")
    
        
        
            
###########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#icon image
icon_image=PhotoImage(file="Images/loginicon.png")
root.iconphoto(False,icon_image)      



img = PhotoImage(file='Images/login icon.png')
Label(root,image=img,bg='#b4c7e7').place(x=70,y=80)

frame=Frame(root,width=350,height=350,bg="#b4c7e7")
frame.place(x=480,y=30)

# heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
# heading.place(x=100,y=5)

#########------------------------------------------------------

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

        
user = Entry(frame,width=22,fg='black',border=0,bg="#e7e6e6",font=('arial',18))
user.place(x=27,y=75)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

###########-----------------------------------------------------
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')



code = Entry(frame,width=22,fg='black',border=0,bg="#e7e6e6",font=('Microsoft YaHei UI Light',18))
code.place(x=27,y=145)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

###############################################################

Button(frame,width=39,pady=7,text='Login',bg='#404040',fg='white',border=0,command=signin).place(x=35,y=214)




root.mainloop()
