import tkinter as ttk
from tkinter import font
att_app=ttk.Tk()
att_app.geometry('800x800')
att_app.title('Attendance System')
font_=font.Font(size=20)

ttk.Label(att_app,text='Face Recognition System',font=font_).pack(expand=True)





att_app.mainloop()