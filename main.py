from tkinter import *
from tkinter import messagebox
import random

win = Tk()
win.title("Strong Password Generator App v-1.0")
win.geometry("800x600")
win.resizable(False, False)

def generate():
    try:
        c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*_-+.,<>/"
        n = int(numofpas.get())
        l = int(lenofpas.get())

        for i in range(n):
            password = ""
            for j in range(l):
                password += random.choice(c)
            result.config(state='normal')
            result.insert(END, f"Password number {i + 1} : {password}\n")
            result.config(state='disabled')
    except:
        messagebox.showerror("Error", "Invalid input! Please enter numbers only.")

f1 = LabelFrame(win, text="Getting info")
f1.pack(expand=True, fill=BOTH, padx=5)

f2 = LabelFrame(win, text="Password Generate")
f2.pack(expand=True, fill=BOTH, padx=5)

p1 = PhotoImage(file="icons8-cyber-security-48.png")
p2 = PhotoImage(file="icons8-safety-care-48.png")
Label(f1, image=p1).place(x=370, y=1)
Label(f2, image=p2).pack()

result = Text(f2, width=45, height=15, bd=0)
result.pack()

Label(f1, text="Enter number of Passwords : ").grid(row=1)
numofpas = Entry(f1)
numofpas.grid(row=1, column=1)

Label(f1, text="Enter length of Password : ").grid(row=2, column=0)
lenofpas = Entry(f1)
lenofpas.grid(row=2, column=1)

Button(f1, text="Click to generate password", command=generate).grid(row=3, column=1, pady=5)

win.mainloop()
