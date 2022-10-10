from curses import window
from tkinter import *
from tkinter import simpledialog
from tokenize import Number
def inputDialog(data, msg=None):
    tempData = simpledialog.askstring("User Input", msg or "Enter numbers seperated by comma")
    try:
        if(tempData != None):
            for i in tempData.strip().split(","):
                data.append(int(i.strip()))
            return True
    except Exception as e:
        return inputDialog(data, msg="Invalid input. Only positive numbers allowed")
    
    # Return denotes if the input is valid
    # So that drawing of data can take place after callback
    return False 
    