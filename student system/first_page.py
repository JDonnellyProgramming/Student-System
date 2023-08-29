#Student System
import tkinter as tk
import math
import subprocess


root = tk.Tk()
root.geometry('600x500')
root.resizable(False, False)


def on_focus_in(event):
   global user_input_color
   print('in')
   print(username_input.get())
   print(user_input_color)
   if username_input.get() == 'Enter Username' and user_input_color == 'grey':
       print('hello')
       username_input.delete(0, tk.END)
       username_input.config(fg='black')
       user_input_color = 'black'


def on_focus_out(event):
   global user_input_color
   print('out')
   if not username_input.get() and user_input_color == 'black':
       username_input.insert(0, 'Enter Username')
       username_input.config(fg='grey')
       user_input_color = 'grey'
def on_pass_in(event):
   global pass_input_color
   if password_input.get() == 'Enter Password' and pass_input_color == 'grey':
       password_input.delete(0, tk.END)
       password_input.config(fg='black')
       pass_input_color = 'black'
def on_pass_out(event):
   global pass_input_color
   if not password_input.get() and pass_input_color == 'black':
       password_input.insert(0, 'Enter Username')
       password_input.config(fg='grey')
       pass_input_color = 'grey'
def Sign_in_click(event=None):
   global new_x1, new_x2, time1
   if (time1 < 43):
       print(time1)
       time1 += 1
       no_account_btn.bind('<Button-1>', no_account_move)
       if (new_x1 <= 600):
           new_x1 += 10
           confirm_pass_lbl.place(x=new_x1, y=290)
       if (new_x2 <= 600):
           new_x2 += 10
           confirm_pass_input.place(x=new_x2, y=330)
       root.after(20, Sign_in_click)
   else:
       no_account_btn.bind('<Button-1>', no_account_click)
       no_account_btn.config(text='Sign Up?')
       login_button.config(text='Login')
       time1 = 0


def no_account_click(event=None):
   global new_x1, new_x2, no_account_clicked, moving_confirm, no_account_move, time1
   print('jj')
   if (time1 < 43):
       time1 += 1
       print(time1)
       no_account_btn.bind('<Button-1>', no_account_move)
       if new_x1 >= 180:
           new_x1 -= 10
           confirm_pass_lbl.place(x=new_x1, y=290)
       if new_x2 >= 160:
           new_x2 -= 10
           confirm_pass_input.place(x=new_x2, y=330)
       root.after(20, no_account_click)
   else:
       no_account_btn.bind('<Button-1>', Sign_in_click)
       no_account_btn.config(text='Sign In?')
       login_button.config(text='Sign Up')
       time1 = 0


def no_account_move(event):
   pass
def login():
   usernames_data = open(r"C:\Users\josep\Downloads\login_stuff.txt").read()
   usernames = usernames_data.split('\n')
   passwords_data = open(r"C:\Users\josep\Downloads\password_stuff.txt").read()
   passwords = passwords_data.split('\n')
   current_username = username_input.get()
   current_password = password_input.get()
   if username_input.get() in usernames:
       if password_input.get() in passwords:
           if usernames.index(username_input.get()) == passwords.index(password_input.get()):
               subprocess.Popen(['python', r'C:\Users\josep\PycharmProjects\pythonProject66\venv\second_page.py'])
               root.destroy()


   else:
               print('Login Unsuccessful')
   print(usernames)
   print(passwords)


time1 = 0
no_account_clicked = False
moving_confirm = False
new_x1 = 600
new_x2 = 600
username_label = tk.Label(root, text='Username', font=('arial', 16, 'normal'))
username_label.place(x=200, y=40)
username_input = tk.Entry(root, font=('arial', 16, 'normal'),
                         fg='grey')
username_input.place(x=160, y=80)
user_input_color = 'grey'
username_focus = False
username_input.insert('insert', 'Enter Username')
username_input.bind('<FocusIn>', on_focus_in)
username_input.bind('<FocusOut>', on_focus_out)


password_label = tk.Label(root, text='Password', font=('arial', 16, 'normal'))
password_label.place(x=200, y=160)
password_input = tk.Entry(root, font=('arial', 16, 'normal'), fg='grey')
password_input.place(x=160, y=200)
pass_input_color = 'grey'
password_focus = False
password_input.insert('insert', 'Enter Password')
password_input.bind('<FocusIn>', on_pass_in)
username_input.bind('<FocusOut>', on_pass_out)


confirm_pass_lbl = tk.Label(root, text='Confirm Password', font=('arial', 16, 'normal'))
confirm_pass_lbl.place(x=new_x1, y=290)#180
confirm_pass_input = tk.Entry(root, font=('arial', 16, 'normal'))
confirm_pass_input.place(x=new_x2, y=330)#160


login_button = tk.Button(root, text='Login', width=20, height=1, command=login)
login_button.place(x=180, y=420)


no_account_btn = tk.Label(root, text='Sign Up?')
no_account_btn.bind('<Button-1>', no_account_click)
no_account_btn.place(x=240, y=460)


root.mainloop()
