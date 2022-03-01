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

        mu = sum(numbers)/len(numbers)
        mean_label = tk.Label(window, text='Mean: ' + str(mu))
        mean_label.pack()   
        sum1 = 0
        for j in range(len(numbers)):
            # Population
            variance = (numbers[j]-mu)**2
            sum1 = sum1 + variance
        population = (cmath.sqrt(sum1/len(numbers)))
        result = tk.Label(window,text='Population: ' + str(population))
        result.pack()
        # Sample
        len_nums = len(numbers)-1
        find_sample = (cmath.sqrt(sum1/len_nums))
        sample_label = tk.Label(window,text='Sample: ' + str(find_sample))
        sample_label.pack()

    except ValueError as e:
        print(e)

button = tk.Button(window,text='Calculate Population & Sample',command=population_deviation)
button.pack()

window.mainloop()
