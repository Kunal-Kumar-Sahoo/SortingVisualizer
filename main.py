from tkinter import *
from tkinter import ttk

# We need to create a random array.
import random

# Importing colors 
from colors import *

# Creating a basic window
window = Tk()
window.title("Sorting Algorithm Visualizer")
window.maxsize(1000, 700)
window.config(bg = WHITE) # Essential for dark mode users.

algorithm_name = StringVar()
# speed
speed_list = ['Fast', 'Medium', 'Slow']

# Random values aka sample data
data = []

# draw the data on the canvas
def drawData(data, colorArray):
    pass

# generate array with random values
def generate():
    pass

# set sorting speed
def set_speed():
    pass

# trigger the selected algorithm and start sorting
def sort():
    pass


# UI here

window.mainloop()
