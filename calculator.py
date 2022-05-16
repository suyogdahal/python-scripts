# coding: utf-8

# In[ ]:


import re

choice = True
previous = 0


def calculate():
    global choice
    global previous
    if previous == 0:
        equation = input("Enter the equation: ")
    else:
        equation = input(str(previous))
    if equation == "quit":
        choice = False
    else:
        new_equation = re.sub('[a-zA-z,():" "]', "", equation)
        if previous == 0:
            previous = eval(new_equation)
            print(previous)
        else:
            previous = eval(str(previous) + equation)


while choice:
    calculate()
