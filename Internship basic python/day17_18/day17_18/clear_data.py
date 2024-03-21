import tkinter as ttk
from tkinter import font
clr_app=ttk.Tk()
clr_app.geometry('800x800')
clr_app.title('Clear Data')
font_=font.Font(size=20)
ttk.Label(clr_app,text='Face Recognition System',font=font_).pack()



clr_app.mainloop()