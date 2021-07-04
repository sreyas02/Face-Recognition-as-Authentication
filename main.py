import sys
import os
from tkinter import *


root = Tk()
root.geometry("340x220")
root.config(bg='light blue')
root.title('ID Authentication')

Label(root, text='Welcome\nFace Recognition System', bg='light blue', font=('caliber', 15, 'bold')).grid(row=0,column=0,columnspan=10)
#name = Entry(root, bg='pink', borderwidth='5',)
def login():
    os.system('login.py')
    os.system('train.py')
def register():
    os.system('register.py')
#def train():
 #   os.system('train.py')
# Buttons
#s1 = Button(root, text='Train Face\n Data', font=("helvetica", 20), height=1, width=10, pady=10, bg="black",
 #           fg='green', command=train)
s2 = Button(root, text='Authenticate\nPerson', font=("helvetica", 20), height=1, width=10, pady=10, bg="black",
            fg='green', command=register)
s3 = Button(root, text='Admin\nControl', font=("helvetica", 20), height=1, width=10, pady=10, bg="black",
            fg='green', command=login)
# add to button

#s1.grid(row=3, column=0)
s2.grid(row=3, column=1)
s3.grid(row=4,column=0)


root.mainloop()
