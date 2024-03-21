import tkinter as ttk
from tkinter import font
from tkinter import messagebox as mb

log_app=ttk.Tk()
log_app.geometry('800x800')
log_app.title('Login Data')
font_=font.Font(size=20)

ttk.Label(log_app,text='Enter Your Credentials',font=font_).pack()


uname=ttk.Variable(log_app)
pwd=ttk.Variable(log_app)

ttk.Label(log_app,text='User Name',font=font_).place(x=100,y=80)
ttk.Entry(log_app,font=font_, textvariable=uname ).place(x=250,y=80)

ttk.Label(log_app,text='Password',font=font_).place(x=100,y=130)
ttk.Entry(log_app,font=font_ , show='🗝️',textvariable=pwd).place(x=250,y=130)

def submit():
    op =''
    with open('opr','r') as f:
        op=f.read()

    if len(op)>0:
        userid=uname.get()
        password=pwd.get()
        p=open('pwd').read()
        if userid == "Khan" and password==p:
            print('login succesfully')
            mb.showinfo('Success', 'Login Successful')
        else:
            print('login failed')
            mb.showerror('Error', 'Login Failed')
            

def back():
    log_app.destroy()
    with open('opr','w') as f:
        f.write('')
    import app

ttk.Button(log_app,text='Submit',command=submit,font=font_,height=1,width=7,bg='#3498DB').place(x=350,y=180)

ttk.Button(log_app,text='Back',command=back,font=font_,height=1,width=7,bg='#3498DB').place(x=350,y=250)

log_app.mainloop()