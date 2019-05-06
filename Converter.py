import tkinter as tk
from tkinter import ttk
import Database as db
from tkinter import messagebox
import sqlite3
from multiprocessing import Process
import webbrowser

# Objective: To convert value from one metric to another
class Converter(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()

        self.Interface_Builder()

    # Objective: Design an Interface
    def Interface_Builder(self):
        self.previous_val=""
        self.operator=""
        self.isrestart="true"

        self.lblfrom = tk.Label(self, text="Convert From")
        self.lblfrom.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

        self.comboconvfrom = tk.ttk.Combobox(self, value=db.populate())
        self.comboconvfrom.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="we")

        self.lblto = tk.Label(self, text="Convert To")
        self.lblto.grid(row=0, column=2, padx=(10, 10), pady=(10, 10))

        self.comboconvto = tk.ttk.Combobox(self,value=db.populate())
        self.comboconvto.grid(row=0, column=3, padx=(10, 10), pady=(10, 10), sticky="we")

        self.lblvalue = tk.Label(self, text="Enter Value")
        self.lblvalue.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

        self.txtvalue = tk.Entry(self, bd=1)
        self.txtvalue.grid(row=1, column=1, padx=(10, 10), pady=(10, 10), columnspan=2, sticky="we")

        self.btnconvert = tk.Button(self, text="Convert", command=lambda: self.btn_convert(self.comboconvfrom.get(),self.comboconvto.get(),self.txtvalue.get()))
        self.btnconvert.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))

        self.btnsave = tk.Button(self, text="Save Result", command=lambda: self.btn_save(self.comboconvfrom.get(),self.comboconvto.get(),self.txtvalue.get()))
        self.btnsave.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))

    # Objective: New Process Function Call to create HTML File of the Result.
    def save_file(self,convert_from,convert_to,value,converted_value):
        html_local='<!DOCTYPE html><html><head><title>Saved Result</title></head><body><h2>Result of the Conversion</h2><b>Value: </b>'+value+'<br><b>Converted From: </b>'+convert_from+'<br><b>Converted To: </b>'+convert_to+'<br><b>Result: </b>'+converted_value+'</body></html>'
        print('Printed by process:', converted_value)
        f = open("result.html", "w")  # relative access
        f.write(html_local)
        f.close()

    # Objective: Get Value from Database to Convert and Calculate it from the Entry to show it to user
    def btn_convert(self,fromvalue,tovalue,value):
        try:
            conn = sqlite3.connect('converter.db')
            cur = conn.cursor()
            # If the values are same in both Combo Box it will multiply value by 1
            if(fromvalue==tovalue):
                valuetom=1.0
                calculated = float(valuetom) * float(value)
            else:
                query = cur.execute('SELECT value FROM converter where conv_from=\''+fromvalue+'\' and conv_to=\''+tovalue+'\'')
                valuetom=query.fetchone()
                calculated = float(valuetom[0]) * float(value)

            tk.messagebox.showinfo('Calculated Value', 'Converted Value:'+str(calculated))
        except Exception:
            tk.messagebox.showerror('Error', 'Cannot calculate the value')

    # Objective: Get Value from Database to Convert, Calculate it from the Entry and Start new Process to Save The Result.
    def btn_save(self,fromvalue,tovalue,value):
        try:
            conn = sqlite3.connect('converter.db')
            cur = conn.cursor()
            # If the values are same in both Combo Box it will multiply value by 1
            if(fromvalue==tovalue):
                valuetom=1.0
                calculated = float(valuetom) * float(value)
            else:
                query = cur.execute('SELECT value FROM converter where conv_from=\''+fromvalue+'\' and conv_to=\''+tovalue+'\'')
                valuetom=query.fetchone()
                calculated = float(valuetom[0]) * float(value)

            #New Process Started
            save_process = Process(target=self.save_file, args=(fromvalue,tovalue,value,str(calculated),))
            save_process.start()
            save_process.join()  # execute next statement when save_process completed
        except Exception:
            tk.messagebox.showerror('Error', 'Cannot calculate the value')








