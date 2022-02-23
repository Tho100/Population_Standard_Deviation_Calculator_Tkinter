import tkinter as tk
from tkinter import *
import cmath

window = Tk()
window.geometry('300x250')
window.title('Population Calculator')

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
            population = (numbers[j]-mu)**2
            sum1 = sum1 + population
        square_root = (cmath.sqrt(sum1))/len(numbers)
        result = tk.Label(window,text=square_root)
        result.pack()

    except ValueError as e:
        print(e)

button = tk.Button(window,text='Calculate Population Standard Deviation',command=population_deviation)
button.pack()

window.mainloop()
