import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
LARGE_FONT = ("Verdana", 12)


class SerialPy(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Empfangen, Senden):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        self.white = True
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Startseite", font=LARGE_FONT)
        self.label.grid(row=0, column=0, padx='5', pady='5', sticky='ew')
        self.label.config(height=1,width=25)
        self.button = tk.Button(self, text="Empfangen",
                           command=lambda: controller.show_frame(Empfangen))
        self.button.config(height = 1, width=40)
        self.button.grid(row=1, column=0, padx='5', pady='5', sticky='ew')
        self.button2 = tk.Button(self, text="Senden",
                            command=lambda: controller.show_frame(Senden))
        self.button2.grid(row=2, column=0, padx='5', pady='5', sticky='ew')
        self.button3 = tk.Button(self, text="Schließen",
                           command=self.client_exit)

        self.button3.grid(row=4, column=0, padx='5', pady='5', sticky='ew')
        self.button4 = tk.Button(self, text="Color-Theme wechseln",
                                 command=self.colorChange)
        self.button4.grid(row=3, column=0, padx='5', pady='5', sticky='ew')


    def client_exit(self):
        exit()

    def colorChange(self):
        if self.white == True:
            Senden.configure(self, background='#303030')
            self.button.configure(bg="#212121", fg="white")
            self.button2.configure(bg="#212121", fg="white")
            self.button3.configure(bg="#212121", fg="white")
            self.button4.configure(bg="#212121", fg="white")
            self.label.configure(bg="#303030", fg="white")
            self.white = False
        elif self.white == False:
            Senden.configure(self, background='white')
            self.button.configure(bg="white", fg="black")
            self.button2.configure(bg="white", fg="black")
            self.button3.configure(bg="white", fg="black")
            self.button4.configure(bg="white", fg="black")
            self.label.configure(bg="white", fg="black")
            self.white = True


class Empfangen(tk.Frame):

    def __init__(self, parent, controller):
        self.white = True
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Empfangen", font=LARGE_FONT)
        self.label.grid(row=0, column=0, padx='5', pady='5', sticky='ew')

        self.button1 = tk.Button(self, text="Startseite",
                           command=lambda: controller.show_frame(StartPage))

        self.button1.grid(row=0, column=1, padx='20', pady='5', sticky='ew')
        self.nachricht = tk.Label(self, text="abc", font=LARGE_FONT)
        self.nachricht.grid(row=1, column=0, padx='5', pady='5', sticky='ew')
        self.nachricht2 = tk.Label(self, text="def", font=LARGE_FONT)
        self.nachricht2.grid(row=2, column=1, padx='5', pady='5', columnspan="2", sticky='ew')
        self.button2 = tk.Button(self, text="Senden",
                            command=lambda: controller.show_frame(Senden))
        self.button2.grid(row=0, column=2, padx='5', pady='5', sticky='ew')
        self.button3 = tk.Button(self, text="Color-Theme wechseln",
                                 command=self.colorChange)
        self.button3.grid(row=3, column=0, padx='5', pady='5', sticky='ew')




    def colorChange(self):
        if self.white == True:
            Senden.configure(self, background='#303030')
            self.button1.configure(bg="#212121", fg="white")
            self.button2.configure(bg="#212121", fg="white")
            self.button3.configure(bg="#212121", fg="white")
            self.label.configure(bg="#303030", fg="white")
            self.white = False
        elif self.white == False:
            Senden.configure(self, background='white')
            self.button1.configure(bg="white", fg="black")
            self.button2.configure(bg="white", fg="black")
            self.button3.configure(bg="white", fg="black")
            self.label.configure(bg="white", fg="black")
            self.white = True



class Senden(tk.Frame):

    def __init__(self, parent, controller):
        self.white = True
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Senden", font=LARGE_FONT)
        self.label.config(anchor='se')
        self.label.grid(row=0, column=0, padx='5', pady='5', sticky='ew')
        self.label2 = tk.Label(self, text="Message:")
        self.label2.grid(row=1, column=0, padx='5', pady='5', sticky='ew')

        self.e1 = ttk.Entry(self)
        self.e1.grid(row=1, column=1, padx='5', pady='5', sticky='ew')
        self.button1 = tk.Button(self, text="Startseite",
                            command=lambda: controller.show_frame(StartPage))

        self.button1.grid(row=0, column=1, padx='5', pady='5', sticky='ew')
        self.button2 = tk.Button(self, text="Empfangen",
                            command=lambda: controller.show_frame(Empfangen))
        self.button2.grid(row=0, column=2, padx='5', pady='5', sticky='ew')
        self.button3 = tk.Button(self, text="Abschicken")
        self.button3.grid(row=2, column=0, padx='5', pady='5', sticky='ew')
        self.button4 = tk.Button(self, text="Color-Theme wechseln",
                                 command=self.colorChange)
        self.button4.grid(row=2, column=1, padx='5', pady='5', sticky='ew')

    def colorChange(self):
        if self.white == True:
            Senden.configure(self, background='#303030')
            self.button1.configure(bg="#212121", fg="white")
            self.button2.configure(bg="#212121", fg="white")
            self.button3.configure(bg="#212121", fg="white")
            self.button4.configure(bg="#212121", fg="white")
            self.label.configure(bg="#303030", fg="white")
            self.label2.configure(bg="#303030", fg="white")
            self.white = False
        elif self.white == False:
            Senden.configure(self, background='white')
            self.button1.configure(bg="white", fg="black")
            self.button2.configure(bg="white", fg="black")
            self.button3.configure(bg="white", fg="black")
            self.button4.configure(bg="white", fg="black")
            self.label.configure(bg="white", fg="black")
            self.label2.configure(bg="white", fg="black")
            self.white = True



app = SerialPy()
app.geometry('300x200')
app.resizable(width=False, height=False)
app.configure(bg="black")
app.mainloop()