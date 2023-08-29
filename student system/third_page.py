import tkinter as tk
import subprocess
#import second_file as sf


graph_window = tk.Tk()
graph_window.geometry('1000x800')
graph_window.resizable(False, False)


def x_axis():
   global curr_x, names_list, grade_nums
   division = 500 / len(names_list)
   for num in range(100):
       label_point = tk.Label(graph_window, text='-')
       label_point.place(x=curr_x, y=400)
       curr_x += 10
   for num1 in range(len(names_list)):
       x_label = tk.Label(graph_window, text=names_list[num1])
       x_label.place(x=500+num1*division, y=460)
def y_axis():
   global curr_y, names_list, grade_nums, y_values
   division = 400 / len(y_values)
   division1 = 400 / 5
   for num in range(100):
       label_point1 = tk.Label(graph_window, text='|')
       label_point1.place(x=500, y=curr_y)
       curr_y += 10
   for num1 in range(len(y_values)):
       y_label = tk.Label(graph_window, text=y_values[num1])
       y_label.place(x=400, y=360-num1*division1)


def plot():
   global names_list, grade_nums
   #global grade_percentage
   person_info = open(r"C:\Users\josep\Downloads\chat_data.txt").read()
   individual_data = person_info.split('\n')
   #print(individual_data)
   for ele in individual_data:
       actual = ele.split(',')
       #print(actual)
       names_list.append(actual[0])
       grade_percentage.append(actual[4])
       #print(names_list)
   for ele1 in names_list:
       namess = ele1.split(' ')
       first_names.append(namess[0])
       second_names.append(namess[1])
       #print(second_names)
   for ele2 in individual_data:
       score = 1
   for ele3 in grade_percentage:
       if (ele3 != '100%'):
           grade_num = ele3[0] + ele3[1]
           grade_nums.append(grade_num)
   print(names_list)
   print(grade_nums)
   x_axis()
   y_axis()
curr_x = 0
curr_y = 0
y_values = [20, 40, 60, 80, 100]
names_list = []
first_names = []
second_names = []
grade_percentage = []
grade_nums = []
plot()
graph_window.mainloop()
