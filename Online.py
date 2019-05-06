import tkinter as tk

from queue import Queue
from threading import Thread
from urllib.request import urlopen
from urllib.parse import quote_plus

import webbrowser


# Objective: To convert value from one metric to another
class Online(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()

        self.Interface_Builder()

    def get_url(self,a_queue, a_url):
        # Pre: a_queue is Queue object and a_url is legitimate URL
        # Post: Content of a_url is at the back of a_queue
        a_queue.put(urlopen(a_url).read())

    # Objective: Design an Interface
    def Interface_Builder(self):
        self.previous_val=""
        self.operator=""
        self.isrestart="true"

        self.lblfrom = tk.Label(self, text="Enter String to Calculate")
        self.lblfrom.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

        self.txtvalue = tk.Entry(self, bd=1)
        self.txtvalue.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), columnspan=2, sticky="we")

        self.btnconvert = tk.Button(self, text="Calculate Online", command=lambda: self.btn_calc(self.txtvalue.get()))
        self.btnconvert.grid(row=1, column=3, padx=(10, 10), pady=(10, 10))

    # Objective: Get Value from Database to Convert and Calculate it from the Entry to show it to user
    def btn_calc(self,txtvalue):
        try:
            text=quote_plus(txtvalue)
            the_urls = ["https://www.google.com/?gws_rd=ssl#q="+str(text)]

            # The content of the first URL in the_urls is on the monitor
            the_queue = Queue()
            for url in the_urls:
                thread = Thread(target=self.get_url, args=(the_queue, url))
                thread.start()
                webbrowser.open_new(url)

        except Exception:
            tk.messagebox.showerror('Error', 'Cannot calculate the value')









