import tkinter as tk




new_window = tk.Tk()
new_window.geometry('1000x800')
new_window.resizable(False, False)




def open_menu():
  global new_width, label1, label2
  if (new_width <= 200):
      menu_button.config(command=opening)
      new_width += 10
      menu_options_frame.config(width=new_width)
      new_window.after(20, open_menu)
  if (new_width >= 200):
      menu_button.config(command=close_menu)
      label1.config(bg='grey')
      label1.config(text='Contact')
      label1.bind('<Enter>', on_enter)
      label1.bind('<Leave>', on_leave)
      label2.config(bg='grey')
      label2.config(text='Graphs')
def on_enter(event=None):
   global new_width1, new_height1, mouse_off, text1, new_text, i
   mouse_off = False
   contact_label.place(x=220, y=200)
   contact_label.config(bd=0)
   if not mouse_off:
       if (new_width1 <= 20) and (new_height1 <= 10):


           #label1.bind('<Enter>', contact_label_opening)
           new_width1 += 2
           new_height1 += 1
           contact_label.config(width=new_width1, height=new_height1)
           new_window.after(10, on_enter)
       if (new_width1 >= 20) and (new_height1 >= 10) and (i < len(text1)):
           new_text += text1[i]
           i += 1
           contact_label.config(text=new_text)
           new_window.after(20, on_enter)




def on_leave(event=None):
   global mouse_off, new_width1, new_height1, text1, new_text, i
   mouse_off = True
   if mouse_off:
       if (new_width1 >= 0) and (new_height1 >= 0):
           new_width1 -= 2
           new_height1 -= 1
           contact_label.config(width=new_width1, height=new_height1)
           new_window.after(10, on_leave)
       if (new_width1 <= 2) and (new_height1 <= 1):
           new_text = ''
           i = 0
           contact_label.config(text='')
           contact_label.config(bd=0)
           #contact_label.place(x=1000, y=200)


def search_bar_func(event):
   global line_count, text2, new_text2, search_names
   names_list = []
   first_names = []
   second_names = []
   #search_names = ''
   search_value = search_bar.get()
   person_data = open(r"C:\Users\josep\Downloads\chat_data.txt").read()
   individual_data = person_data.split('\n')
   for ele in individual_data:
       actual = ele.split(',')
       names_list.append(actual[0])
   for ele1 in names_list:
       namess = ele1.split(' ')
       first_names.append(namess[0])
       second_names.append(namess[1])
   if (search_names < )
   for index, name in enumerate(first_names):
       if search_value.lower() in name.lower():
           new_name1 = name + ' ' + second_names[index]
           #print(new_name1)
   for index, second in enumerate(second_names):
       if search_value.lower() in second.lower():
           new_name2 = first_names[index] + ' ' + second
           #print(new_name2)
   if new_name1 != '':
       search_names += new_name1
   if search_names != '':
       print(search_names)


   if len(search_value) > 0:
       search_label.place(x=750, y=79)
   else:
       search_label.place_forget()


def opening():
  pass
def close_menu():
  global new_width, label1, label2
  label1.config(bg='white')
  label1.config(text='')
  label2.config(bg='white')
  label2.config(text='')
  if (new_width >= 0):
      menu_button.config(command=opening)
      new_width -= 10
      menu_options_frame.config(width=new_width)
      new_window.after(20, close_menu)
  if (new_width <= 0):
      menu_button.config(command=open_menu)
      label1.config(bg='white')
      label1.config(text='')
      label2.config(bg='white')
      label2.config(text='')
mouse_off = True
new_text = ''
i = 0
new_width = 0
new_width1 = 0
new_height1 = 0
line_count = 0
search_names = ''
text1 = 'You can contact us\nat 0788955595 or if\nyou would like to leave\nan email the contact is\nat student@kingsway.com'
text2 = ''
new_text2 = ''
new_height2 = 1
top_frame = tk.Frame(new_window, bg='blue', height=100)
top_frame.pack(side=tk.TOP, fill=tk.X)
search_bar = tk.Entry(new_window, width=30)
search_bar.bind('<KeyRelease>', search_bar_func)
search_bar.place(x=750, y=60)
search_button = tk.Button(new_window, width=4, height=1, text='search')
search_button.place(x=938, y=60)


menu_button = tk.Button(new_window, width=4, height=1, text='|||', command=open_menu)
menu_button.place(x=30, y=60)
menu_options_frame = tk.Frame(new_window, bg='grey', width=new_width)
menu_options_frame.pack(side=tk.LEFT, fill=tk.Y)
label1 = tk.Label(new_window, text='', bg='white', font=('arial', 16, 'normal'))
label1.place(x=40, y=200)
label2 = tk.Label(new_window, text='', bg='white', font=('arial', 16, 'normal'))
label2.place(x=40, y=240)
contact_label = tk.Label(new_window, bg='white', bd=1, relief='solid',
                        width=new_width1, height=new_height1,
                        text='')
contact_label.place(x=1000, y=200)#x=220
search_label = tk.Label(new_window, bg='white', bd=1, relief='solid',
                       width=26, height=new_height2, text='')
search_label.place(x=1000, y=79)#x=750


new_window.mainloop()
