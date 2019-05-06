import tkinter as tk

# Objective: To Calculate values input by user
class Interface(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()

        self.Interface_Builder()

    # Objective: Design an Interface
    def Interface_Builder(self):
        self.previous_val=""
        self.operator=""
        self.isrestart="true"

        self.txtanswer=tk.Entry(self,bd=1,state="disabled",disabledforeground="black",justify="right")
        self.txtanswer.grid(row=0,column=0,padx=(10, 10),pady=(10, 10),columnspan=4,sticky="we")

        self.btnac=tk.Button(self,text="AC",command=lambda:self.btn_callback("AC"))
        self.btnac.grid(row=1,column=0,padx=(10, 10),pady=(10, 10))

        self.btnplusminus=tk.Button(self,text="+/-",command=lambda:self.btn_callback("-"))
        self.btnplusminus.grid(row=1,column=1,padx=(10, 10),pady=(10, 10))

        self.btnpercent=tk.Button(self,text="%",command=lambda:self.btn_callback("%"))
        self.btnpercent.grid(row=1,column=2,padx=(10, 10),pady=(10, 10))

        self.btndivide=tk.Button(self,text="/",command=lambda:self.btn_callback("/"))
        self.btndivide.grid(row=1,column=3,padx=(10, 10),pady=(10, 10))


        self.btn7=tk.Button(self,text="7",command=lambda:self.btn_callback("7"))
        self.btn7.grid(row=2,column=0,padx=(10, 10),pady=(10, 10))

        self.btn8=tk.Button(self,text="8",command=lambda:self.btn_callback("8"))
        self.btn8.grid(row=2,column=1,padx=(10, 10),pady=(10, 10))

        self.btn9=tk.Button(self,text="9",command=lambda:self.btn_callback("9"))
        self.btn9.grid(row=2,column=2,padx=(10, 10),pady=(10, 10))

        self.btnmulti=tk.Button(self,text="X",command=lambda:self.btn_callback("*"))
        self.btnmulti.grid(row=2,column=3,padx=(10, 10),pady=(10, 10))

        self.btn4=tk.Button(self,text="4",command=lambda:self.btn_callback("4"))
        self.btn4.grid(row=3,column=0,padx=(10, 10),pady=(10, 10))

        self.btn5=tk.Button(self,text="5",command=lambda:self.btn_callback("5"))
        self.btn5.grid(row=3,column=1,padx=(10, 10),pady=(10, 10))

        self.btn6=tk.Button(self,text="6",command=lambda:self.btn_callback("6"))
        self.btn6.grid(row=3,column=2,padx=(10, 10),pady=(10, 10))

        self.btnsub=tk.Button(self,text="-",command=lambda:self.btn_callback("-"))
        self.btnsub.grid(row=3,column=3,padx=(10, 10),pady=(10, 10))

        self.btn1=tk.Button(self,text="1",command=lambda:self.btn_callback("1"))
        self.btn1.grid(row=4,column=0,padx=(10, 10),pady=(10, 10))

        self.btn2=tk.Button(self,text="2",command=lambda:self.btn_callback("2"))
        self.btn2.grid(row=4,column=1,padx=(10, 10),pady=(10, 10))

        self.btn3=tk.Button(self,text="3",command=lambda:self.btn_callback("3"))
        self.btn3.grid(row=4,column=2,padx=(10, 10),pady=(10, 10))

        self.btnadd=tk.Button(self,text="+",command=lambda:self.btn_callback("+"))
        self.btnadd.grid(row=4,column=3,padx=(10, 10),pady=(10, 10))

        self.btn0=tk.Button(self,text="0",command=lambda:self.btn_callback("0"))
        self.btn0.grid(row=5,column=0,columnspan=2,padx=(10, 10),pady=(10, 10),sticky="we")

        self.btndecimal=tk.Button(self,text=".",command=lambda:self.btn_callback("."))
        self.btndecimal.grid(row=5,column=2,padx=(10, 10),pady=(10, 10))

        self.btnequal=tk.Button(self,text="=",command=lambda:self.btn_callback("="))
        self.btnequal.grid(row=5,column=3,padx=(10, 10),pady=(10, 10))

    # Objective: Button Event Handler which inputs the value into textbox if the button clicked belong to the values
    # or
    # It calculates the entered value from the stack if the operator button is clicked and input into textbox
    def btn_callback(self,val):

        if(val=="1" or val=="2" or val=="3" or val=="4" or val=="5" or val=="6" or val=="7" or val=="8" or val=="9" or val=="0"):
            if(self.isrestart!="true"):
                self.txtanswer.config(state="normal")
                self.txtanswer.insert("end",val)
                self.txtanswer.config(state="disabled")
            else:
                self.txtanswer.config(state="normal")
                self.txtanswer.delete(0,"end")
                self.txtanswer.insert("end",val)
                self.isrestart="false"
                self.txtanswer.config(state="disabled")
        elif(val== "+" or val== "-" or val== "*" or val== "/" or val== "="):

            self.previous_val=self.previous_val+self.txtanswer.get()
            print(self.previous_val[:-1])
            try:
                evaluated=eval(self.previous_val)
                if(val!="="):
                    self.previous_val=str(evaluated)+val
                else:
                    self.previous_val=""
                    self.txtanswer.config(state="normal")
                    self.txtanswer.delete(0,"end")
                    self.txtanswer.insert("end",evaluated)
                    self.txtanswer.config(state="disabled")
            except ZeroDivisionError:
                print("Cannot Divide by Zero")
                evaluated=self.previous_val[:-2]
                if(val!="="):
                    self.previous_val=str(evaluated)+val
                else:
                    self.previous_val=""
                    self.txtanswer.config(state="normal")
                    self.txtanswer.delete(0,"end")
                    self.txtanswer.insert("end",evaluated)
                    self.txtanswer.config(state="disabled")
            except:
                self.previous_val=self.previous_val+val


            self.isrestart="true"
        elif(val=="AC"):
            self.isrestart="true"
            self.previous_val=""
            self.txtanswer.config(state="normal")
            self.txtanswer.delete(0,"end")
            self.txtanswer.insert("end","")
            self.txtanswer.config(state="disabled")




