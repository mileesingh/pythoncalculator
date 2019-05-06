import tkinter as tk
from Interface import Interface
from Converter import Converter
from Online import Online
# Objective: Show Interface with two buttons to open Calculator or Converter

class Main_Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.Interface_Builder()

    def Interface_Builder(self):
        self.btn_calc = tk.Button(self, text="Open Calculator", command=lambda: self.open_calc())
        self.btn_calc.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="we")

        self.btn_conv = tk.Button(self, text="Open Converter", command=lambda: self.open_conv())
        self.btn_conv.grid(row=1, column=1, padx=(10, 10), pady=(10, 10))

        self.btn_online = tk.Button(self, text="Calculate Online", command=lambda: self.open_online())
        self.btn_online.grid(row=1, column=2, padx=(10, 10), pady=(10, 10))


    def open_calc(self):
        root = tk.Tk()
        root.title("Calculator")
        app = Interface(master=root)
        app.mainloop()

    def open_conv(self):
        root = tk.Tk()
        root.title("Converter")
        app = Converter(master=root)
        app.mainloop()

    def open_online(self):
        root = tk.Tk()
        root.title("Online Calculator")
        app = Online(master=root)
        app.mainloop()


root = tk.Tk()
root.title("Choose Option")
app = Main_Window(master=root)

app.mainloop()
