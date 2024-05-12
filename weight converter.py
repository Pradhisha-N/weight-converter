#importing tkinter module
import tkinter as tk
from tkinter import *

window=Tk()#creating a window
window.title("PythonGeeks")#title of the window
window.geometry("500x500")#geometry of the window
#create a label
Label(window,text="WEIGHT CONVERTER",font=("Arial", 20 ),bg="black",fg='yellow').pack()

kg=tk.IntVar()#kg is integer type

def convert_to_gram():
    kg1=kg.get() #getting the value
    gram = float(kg1)*1000 #convert to float
    Label(window,text="This weight in grams would be",font=("Arial", 12 )).pack()
    Label(window,text=gram,bg="red").pack()

def convert_to_ounce():
    kg1=kg.get()#getting the value
    ounce = float(kg1)*35.274#convert to float
    Label(window,text="This weight in ounce would be",font=("Arial", 12 )).pack()
    Label(window,text=ounce,bg="red").pack()

def convert_to_pound():
    kg1=kg.get()#getting the value
    pound = float(kg1)*2.20462#convert to float
    Label(window,text="This weight in pound would be",font=("Arial", 12 )).pack()
    Label(window,text=pound,bg="red").pack()

Label(window,text="Enter the weight in Kgs",font=("Arial", 14 )).pack()
Entry(window,textvariable=kg).pack()#entry field
#creating buttons
Button(window,text="Convert to Gram",bg="blue",command=convert_to_gram).pack()
Button(window,text="Convert to Ounce",bg="blue",command=convert_to_ounce).pack()
Button(window,text="Convert to Pound",bg="blue",command=convert_to_pound).pack()

window.mainloop()
