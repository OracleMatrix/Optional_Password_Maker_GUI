from customtkinter import *
from tkinter import messagebox
import random

root = CTk()
root.title('Strong Password Generator App v-1.2')
root.geometry('450x450')
root.resizable(False, False)
root.attributes('-alpha', 0.8)

t = 0


def theme():
    global t
    if t == 0:
        set_appearance_mode("dark")
        t += 1
    else:
        set_appearance_mode("light")
        t -= 1


app_name_label = CTkLabel(root, text='Password Generator', font=('Century Gothic', 20))
app_name_label.place(relx=0.1, rely=0.06, anchor='nw')

theme_switch = CTkSwitch(root, text='Dark', switch_height=15, switch_width=28, corner_radius=15, command=theme,
                         button_color="purple", button_hover_color="purple", progress_color="#d993eb")
theme_switch.place(relx=0.75, rely=0.05)

length_label = CTkLabel(root, text='Length', font=('Century Gothic', 10))
length_label.place(relx=0.1, rely=0.18, anchor='nw')

slider_var = IntVar()
length_slider = CTkSlider(root, width=360, border_width=0, progress_color="#d993eb", button_color="purple",
                          button_hover_color="purple", fg_color=("#d3d3d5", "#363037"), from_=8, to=20,
                          variable=slider_var)
length_slider.place(relx=0.1, rely=0.27, anchor='nw')

textbox_slider = CTkTextbox(root, font=('Century Gothic', 10), width=70, height=30, corner_radius=5,
                            border_width=2, state='disabled')
textbox_slider.place(relx=0.73, rely=0.19, anchor='nw')


def update_slider_text(event):
    textbox_slider.configure(state='normal')
    textbox_slider.delete(1.0, 'end')
    textbox_slider.insert('end', int(length_slider.get()))
    textbox_slider.configure(state='disabled')


length_slider.bind("<B1-Motion>", update_slider_text)

checkbox_var = IntVar()
numbers_checkbox = CTkCheckBox(root, text='Numbers', font=('Century Gothic', 10), border_width=2, variable=IntVar())

numbers_checkbox.place(relx=0.1, rely=0.35, anchor='nw')

small_letters_checkbox = CTkCheckBox(root, text="Small Letters", font=('Century Gothic', 10), border_width=2,
                                     variable=IntVar())
small_letters_checkbox.place(relx=0.1, rely=0.43, anchor='nw')

capital_letters_checkbox = CTkCheckBox(root, text="Capital Letters", font=('Century Gothic', 10), border_width=2,
                                       variable=IntVar())
capital_letters_checkbox.place(relx=0.1, rely=0.51, anchor='nw')

special_chars_checkbox = CTkCheckBox(root, text="Special Characters", font=('Century Gothic', 10), border_width=2,
                                     variable=IntVar())
special_chars_checkbox.place(relx=0.1, rely=0.59, anchor='nw')

just_numbers = "1234567890"
small_letters = "abcdefghijklmnopqrstuvwxyz"
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_letters = "!@#$%^&*_-+?"

length = int(length_slider.get())
num = 1

mix0 = [just_numbers, small_letters, capital_letters, special_letters]
mix1 = [just_numbers, small_letters, capital_letters]
mix2 = [special_letters, small_letters, capital_letters]
mix3 = [just_numbers, special_letters, capital_letters]
mix4 = [just_numbers, special_letters]
mix5 = [just_numbers, small_letters]
mix6 = [just_numbers, capital_letters]
mix7 = [just_numbers, special_letters, small_letters]
mix8 = [small_letters, capital_letters]
mix9 = [small_letters, special_letters]
mix10 = [capital_letters, special_letters]


def generate():
    global length
    if textbox_slider.get("1.0", "end-1c") == "":
        messagebox.showerror("Error", "Please Select length of the password!")
    elif numbers_checkbox.get() == 0 and small_letters_checkbox.get() == 0 and capital_letters_checkbox.get() == 0 and special_chars_checkbox.get() == 0:
        messagebox.showerror("Error", "Please select at least one option")
    length = int(textbox_slider.get("1.0", "end-1c"))
    if numbers_checkbox.get() == 1:
        for i in range(num):
            password = ""
            for j in range(length):
                password += random.choice(just_numbers)
            generated_password_textbox.delete(1.0, 'end')
            generated_password_textbox.insert(INSERT, password)
    if small_letters_checkbox.get() == 1:
        for i in range(num):
            password = ""
            for j in range(length):
                password += random.choice(small_letters)
            generated_password_textbox.delete(1.0, 'end')
            generated_password_textbox.insert(INSERT, password)
    if capital_letters_checkbox.get() == 1:
        for i in range(num):
            password = ""
            for j in range(length):
                password += random.choice(capital_letters)
            generated_password_textbox.delete(1.0, 'end')
            generated_password_textbox.insert(INSERT, password)
    if special_chars_checkbox.get() == 1:
        for i in range(num):
            password = ""
            for j in range(length):
                password += random.choice(special_letters)
            generated_password_textbox.delete(1.0, 'end')
            generated_password_textbox.insert(INSERT, password)
    if small_letters_checkbox.get() == 1 and capital_letters_checkbox.get() == 1 and special_chars_checkbox.get() == 1:
        for i in range(num):
            password = ""
            for j in range(length):
                password += random.choice("".join(mix2))
            generated_password_textbox.delete(1.0, 'end')
            generated_password_textbox.insert(INSERT, password)
    if numbers_checkbox.get() == 1 and capital_letters_checkbox.get() == 1 and special_chars_checkbox.get() == 1:
        for i in range(num):
            password = ""
            for j in range(length):
                password += random.choice("".join(mix3))
            generated_password_textbox.delete(1.0, 'end')
            generated_password_textbox.insert(INSERT, password)
    if numbers_checkbox.get() == 1 and special_chars_checkbox.get() == 1:
        for i in range(num):
            password = ""
            for j in range(length):
                password += random.choice("".join(mix4))
            generated_password_textbox.delete(1.0, 'end')
            generated_password_textbox.insert(INSERT, password)
    if numbers_checkbox.get() == 1 and small_letters_checkbox.get() == 1:
        for i in range(num):
            password = ""
            for j in range(length):
                password += random.choice("".join(mix5))
            generated_password_textbox.delete(1.0, 'end')
            generated_password_textbox.insert(INSERT, password)
    if numbers_checkbox.get() == 1 and capital_letters_checkbox.get() == 1:
        for i in range(num):
            password = ""
            for j in range(length):
                password += random.choice("".join(mix6))
            generated_password_textbox.delete(1.0, 'end')
            generated_password_textbox.insert(INSERT, password)
    if numbers_checkbox.get() == 1 and small_letters_checkbox.get() == 1 and special_chars_checkbox.get() == 1:
        for i in range(num):
            password = ""
            for j in range(length):
                password += random.choice("".join(mix7))
            generated_password_textbox.delete(1.0, 'end')
            generated_password_textbox.insert(INSERT, password)
    if small_letters_checkbox.get() == 1 and capital_letters_checkbox.get() == 1:
        for i in range(num):
            password = ""
            for j in range(length):
                password += random.choice("".join(mix8))
            generated_password_textbox.delete(1.0, 'end')
            generated_password_textbox.insert(INSERT, password)
    if small_letters_checkbox.get() == 1 and special_chars_checkbox.get() == 1:
        for i in range(num):
            password = ""
            for j in range(length):
                password += random.choice("".join(mix9))
            generated_password_textbox.delete(1.0, 'end')
            generated_password_textbox.insert(INSERT, password)
    if capital_letters_checkbox.get() == 1 and special_chars_checkbox.get() == 1:
        for i in range(num):
            password = ""
            for j in range(length):
                password += random.choice("".join(mix10))
            generated_password_textbox.delete(1.0, 'end')
            generated_password_textbox.insert(INSERT, password)
    if numbers_checkbox.get() == 1 and small_letters_checkbox.get() == 1 and capital_letters_checkbox.get() == 1:
        for i in range(num):
            password = ""
            for j in range(length):
                password += random.choice("".join(mix1))
            generated_password_textbox.delete(1.0, 'end')
            generated_password_textbox.insert(INSERT, password)
    if numbers_checkbox.get() == 1 and small_letters_checkbox.get() == 1 and capital_letters_checkbox.get() == 1 and special_chars_checkbox.get() == 1:
        for i in range(num):
            password = ""
            for j in range(length):
                password += random.choice("".join(mix0))
            generated_password_textbox.delete(1.0, 'end')
            generated_password_textbox.insert(INSERT, password)


def check_pass_power():
    top = CTkToplevel(root)
    top.title("Password Power Checker")
    top.geometry("400x400")
    top.attributes("-topmost", True)
    top.attributes('-alpha', 0.9)
    top.resizable(False, False)
    insert_password_label = CTkLabel(top, text="Insert Password", font=('Century Gothic', 20))
    insert_password_label.place(relx=0.5, rely=0.2, anchor='c')
    pass_entry = CTkEntry(top, font=('Century Gothic', 15), width=300, corner_radius=10, height=40)
    pass_entry.place(relx=0.5, rely=0.3, anchor='c')
    result_label = CTkLabel(top, text="")
    result_label.place(relx=0.5, rely=0.6, anchor='c')

    def password_checker():
        data = pass_entry.get()

        if len(data) < 8:
            result_label.configure(top, text="Bad : \nPassword length should be at least 8 characters.",
                                   text_color="red",
                                   font=('Century Gothic', 15))



        elif data.isdigit():
            result_label.configure(top, text="Weak : \nPassword should not be only numbers.", text_color="yellow",
                                   font=('Century Gothic', 15))

        elif not any(char.isupper() for char in data):
            result_label.configure(top,
                                   text="Medium : \nit could be at least with one uppercase letter or special character.",
                                   text_color="yellow", font=('Century Gothic', 11))

        elif not any(char.islower() for char in data):
            result_label.configure(top,
                                   text="Medium : \nit could be at least with one lowercase letter or special character",
                                   text_color="yellow", font=("Century Gothic", 11))

        elif not any(char in special_letters for char in data):
            result_label.configure(top, text="strong : \nPassword is good but could be better with special character.",
                                   text_color="#a2db80", font=("Century Gothic", 12))

        else:
            result_label.configure(top, text="Super strong : \nPassword is very strong!", text_color="green",
                                   font=("Century Gothic", 15))

    check_pass_button = CTkButton(top, text="Check Power", corner_radius=20, height=35, fg_color="purple",
                                  hover_color="#b33fd0", width=200, font=('Century Gothic', 13),
                                  command=password_checker)
    check_pass_button.place(relx=0.5, rely=0.42, anchor='c')

    check_pass_button = CTkButton(top, text="Check Power", corner_radius=20, height=35, fg_color="purple",
                                  hover_color="#b33fd0", width=200, font=('Century Gothic', 13),
                                  command=password_checker)
    check_pass_button.place(relx=0.5, rely=0.42, anchor='c')


generate_button = CTkButton(root, text="Generate", font=('Century Gothic', 10), width=180, fg_color="purple",
                            hover_color="#b33fd0", height=35, command=generate)
generate_button.place(relx=0.1, rely=0.67, anchor='nw')

check_password_power = CTkButton(root, text="Check Password Power", font=('Century Gothic', 10), width=180,
                                 fg_color="purple", hover_color="#b33fd0", height=35, command=check_pass_power)
check_password_power.place(relx=0.52, rely=0.67, anchor='nw')

generated_password_textbox = CTkTextbox(root, font=('Century Gothic', 10), height=70, corner_radius=15, width=370,
                                        border_width=2)
generated_password_textbox.place(relx=0.1, rely=0.77, anchor='nw')

root.mainloop()
