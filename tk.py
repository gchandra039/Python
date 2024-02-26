from tkinter import *
import sqlite3

root = Tk()
root.geometry('410x450')
root.title("database")

root.configure(background='lightpink')

textin=StringVar()
textinn=StringVar()

menu=Menu(root)
root.config(menu=menu)

menu=Menu(root)
root.config(menu=menu)

lab=Label(root,text='Name:',font=('none 13 bold'))
lab.place(x=0,y=10)

entname=Entry(root,width=20,font=('none 13 bold'),textvar=textin)
entname.place(x=80,y=10)

entphone=Entry(root,width=20,font=('none 13 bold'),textvar=textinn)
entphone.place(x=80,y=50)

lab1=Label(root,text='Phone:',font=('none 13 bold'))
lab1.place(x=0,y=50)

db = sqlite3.connect('mysq.db')
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS People(name TXT, phone TXT)')
db.commit()

def insert():
  name1 = textin.get()
  phone1 = textinn.get()
  conn = sqlite3.connect('mysq.db')
  with conn:
    cursor = conn.cursor()
    cursor.execute('INSERT INTO People(name, phone) values(?,?)',(name1,phone1))
    db.close()


def show():
  conn=sqlite3.connect('mysq.db')
  cursor=conn.cursor()
  cursor.execute('SELECT * FROM People')
  for i in cursor.fetchall():
    print(i) 
    
name = StringVar()
phone = StringVar()
def update():
  nam = name.get()
  pho = phone.get()
  conn = sqlite3.connect('mysq.db')
  with conn:
    cursor = conn.cursor()
    cursor.execute('UPDATE People SET name=? WHERE phone=?',(nam,pho))
    conn.commit()


def drop():
  conn = sqlite3.connect('mysq.db')
  cursor = conn.cursor()
  cursor.execute('DROP TABLE People')
  conn.commit()

deName=StringVar()
def delete():
  dee=deName.get()
  conn = sqlite3.connect('mysq.db')
  cursor = conn.cursor()
  cursor.execute('DELETE FROM People WHERE name = ?',(dee,))
  conn.commit()

labdel=Label(root,text="DeleName",font=('non 13 bold'))
labdel.place(x=10,y=350)

entDel=Entry(root,width=20,font=('non 13 bold'),textvar=deName)
entDel.place(x=100,y=350)

buttdel=Button(root,padx=2,pady=2,text='Delete',command=delete,font=('non 13 bold'),relief='raised')
buttdel.place(x=100,y=400)

enterupName=Entry(root,width=20,font=('non 13 bold'),textvar=name)
enterupName.place(x=150,y=200)

enterPho=Entry(root,width=20,font=('non 13 bold'),textvar=phone)
enterPho.place(x=150,y=250)

buttsubmit=Button(root,padx=2,pady=2,text='submit',command=insert,font=('non 13 bold'),relief='raise',background='blue')
buttsubmit.place(x=60,y=100)

buttshow=Button(root,padx=2,pady=2,text='show',command=show,font=('non 13 bold'),relief='raise')
buttshow.place(x=200,y=100)

buttupdate=Button(root,padx=2,pady=2,text='Update',command=update,font=('non 13 bold'),relief='raised')
buttupdate.place(x=250,y=300)

lab3=Label(root,text='UpdateName',font=('non 13 bold'))
lab3.place(x=10,y=200)
lab3=Label(root,text='Phonenumber',font=('non 13 bold'))
lab3.place(x=10,y=250)

root.mainloop()