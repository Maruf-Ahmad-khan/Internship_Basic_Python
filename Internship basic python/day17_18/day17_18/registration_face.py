import tkinter as ttk
from tkinter import font
from tkinter import messagebox as mb
reg_app=ttk.Tk()
reg_app.geometry('800x800')
reg_app.title('Registration Face')
font_=font.Font(size=20)

ttk.Label(reg_app,text='Face Recognition System',font=font_).pack()
userid = uname.get()
password = pwd.get()
p = open('pwd').read()
if userid == 'admin' and password == p:
     print('login successful')
     mb.showinfo('successs', 'Login Successful')
     from tkinter.simpledialog import askstring
     name = askstring('Name', 'For whom you want to register?')
     print(name) #take this forward
else:
     print('Login failed')
     mb.showerror('Error', 'Login Failed')



reg_app.mainloop()