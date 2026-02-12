from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
screen=Tk()
screen.geometry("600x600")
screen.config(background="light blue",border=20, borderwidth=5, relief="groove")
screen.title("Basic Widgets")


username=Entry(screen)
username.place(x=120,y=100)
Entry(screen, show="*").place(x=120,y=140)
Label(screen,text="Username").place(x=50,y=100)
Label(screen,text="Password").place(x=50,y=140)

def messages():
     username_value=username.get()
     messagebox.showinfo("info message", "Welcome"  + username_value)
     a=messagebox.askyesno("yes no", "is it okay to move forward")
     print(a)

Button(screen,background="green",text="Login",command=messages).place(x=250,y=200)


#Button(screen,text="login",command=messages).place(x=250,y=250)
screen.mainloop()