import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def run_calculation():
    x = float(mile_entry.get())
    x *= 1.60934
    km["text"] = round(x,2)

mile_label = ttk.Label(text="Miles")
mile_label.grid(column=2, row=0)

mile_entry = ttk.Entry(width=7)
mile_entry.grid(column=1,row=0)

is_equal_to = ttk.Label(text="is equal to")
is_equal_to.grid(column=0,row=1)

km = ttk.Label(text=0)
km.grid(column=1, row=1)

km_label = ttk.Label(text="Km")
km_label.grid(column=2, row=1)

button = ttk.Button(text="Calculate", command=run_calculation)
button.grid(column=1, row=2)

window.mainloop()