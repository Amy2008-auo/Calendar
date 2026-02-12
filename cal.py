from tkinter import *
import calendar
screen=Tk()
screen.geometry("600x600")
screen.config(background="light grey",border=20, borderwidth=5, relief="groove")
screen.title("calendar")

def show_calendar():
    screen2=Tk()
    screen2.geometry("600x600")
    y=year.get()
    y=int(y)
    print(calendar.calendar(y))
    calendar_data=calendar.calendar(y)
    l=Label(screen2, text=calendar_data,font="Consolas 10 bold")
    l.grid(row=5,column=1,padx=20)
    screen2.mainloop()

Label(screen,text="Calendar").pack(pady=20)
Label(screen,text="Enter the year").pack(side=TOP,pady=20)
year=Entry(screen)
year.pack(pady=20)
Button(screen,background="green",text="Show calendar",command=show_calendar).pack(pady=20)
Button(screen,background="green",text="exit", command=exit).pack(pady=20)





screen.mainloop()