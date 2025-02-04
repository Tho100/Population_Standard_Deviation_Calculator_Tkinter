import tkinter as tk
from tkinter import *
import cmath
import matplotlib.pyplot as plt 
import pandas as pd 

window = Tk()
window.geometry('330x250')
window.title('Standard Deviation Calculator')

insert_n = tk.Entry(window)
insert_n.pack()

def population_deviation():
    try:
        
        numbers = [int(x.strip()) for x in insert_n.get().strip().split(',')]

        mean = np.sum(numbers)/len(numbers)
        
        mean_label = tk.Label(window, text='Mean: ' + str(mean))
        mean_label.pack()   

        variance = np.sum((numbers - mean) ** 2)
        std_deviation = np.sqrt(variance / len(numbers))

        result = tk.Label(window,text='Standard Deviation: ' + str(std_deviation))
        result.pack()

        sample_variance = variance / len(numbers) - 1

        sample_label = tk.Label(window,text='Sample: ' + str(sample_variance))
        sample_label.pack()

    except ValueError as e:
        print(e)

button = tk.Button(window,text='Calculate Population & Sample',command=population_deviation)
button.pack()

window.mainloop()
