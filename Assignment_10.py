import tkinter as t
import webbrowser as w

a = t.Tk(className="Assignment 10")


label = t.Label(a, text="Enter a channel to search", font=("Times New Roman" , 18))
label.grid()
string = t.Entry(a, font=("Times New Roman", 19), width=40)
string.grid()

def display():
    destination = string.get()
    print(f"navigating to https://youtube.com/@{destination}")
    w.open("https://youtube.com/@" + destination)

b = t.Button(a, text="Search", font=("Times New Roman", 20), command=display)
b.grid()


a.mainloop()