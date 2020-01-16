import tkinter as tk
from tkinter import ttk, Menu
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
        self.label.grid(row=0, column=0, padx='100', pady='5', sticky='ew')
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
        self.nachrichten = tk.Frame(self)
        self.nachrichten.grid(row=1, column=0,)
        testdaten = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ"]
        testdaten2 = [("ABC","A"),("123","B"),("DEF","B"),("XYZ","A")]
        for i in range(len(testdaten2)):
            print("ABC")
            column = 0
            if testdaten2[i][1] == "A":
                print("links")
                column = 0
            if testdaten2[i][1] == "B":
                print("rechts")
                column = 1
            self.name = tk.Label(self.nachrichten, text={testdaten[i]}, font=LARGE_FONT)
            self.name.grid(row=i, column=column)
            #for i in range(len(testdaten)):
                #print(testdaten[i])
                #row = i
                #if i % 2 == 0:
                    #column = 0
                #else:
                    #column = 1
                #name = 'label{i}'
                #self.name = tk.Label(self.nachrichten, text={testdaten[i]}, font=LARGE_FONT)
                #self.name.grid(row=row, column=column)

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
        self.button3.grid(row=2, column=0, padx='5', pady=(5,50), sticky='ew')
        self.button4 = tk.Button(self, text="Color-Theme wechseln",
                                 command=self.colorChange)
        self.button4.grid(row=2, column=1, padx='5', pady=(5,50), sticky='ew')
        #self.separator = ttk.Separator(self, orient="horizontal")
        #self.separator.grid(row=4, column=1, sticky="we")
        self.label3 = tk.Label(self, text="Baud-Rate:")
        self.label3.grid(row=5, column=0, padx='5', pady='5', sticky='ew')
        self.label3.config(height=1, width=5)
        self.e2 = ttk.Entry(self, width=1)
        self.e2.grid(row=5, column=1, padx='5', pady='5', sticky='ew')
        self.label4 = tk.Label(self, text="Stopbits:")
        self.label4.grid(row=5, column=2, padx='5', pady='5', sticky='ew')
        self.label4.config(height=1, width=5)
        self.e3 = ttk.Entry(self, width=5)
        self.e3.grid(row=5, column=3, padx='5', pady='5', sticky='ew')
        self.label5 = tk.Label(self, text="Databits:")
        self.label5.grid(row=5, column=4, padx='5', pady='5', sticky='ew')
        self.label5.config(height=1, width=5)
        self.e4 = ttk.Entry(self, width=5)
        self.e4.grid(row=5, column=5, padx='5', pady='5', sticky='ew')


    def colorChange(self):
        if self.white == True:
            Senden.configure(self, background='#303030')
            self.button1.configure(bg="#212121", fg="white")
            self.button2.configure(bg="#212121", fg="white")
            self.button3.configure(bg="#212121", fg="white")
            self.button4.configure(bg="#212121", fg="white")
            self.label.configure(bg="#303030", fg="white")
            self.label2.configure(bg="#303030", fg="white")
            self.label3.configure(bg="#303030", fg="white")
            self.label4.configure(bg="#303030", fg="white")
            self.label5.configure(bg="#303030", fg="white")
            self.white = False
        elif self.white == False:
            Senden.configure(self, background='white')
            self.button1.configure(bg="white", fg="black")
            self.button2.configure(bg="white", fg="black")
            self.button3.configure(bg="white", fg="black")
            self.button4.configure(bg="white", fg="black")
            self.label.configure(bg="white", fg="black")
            self.label2.configure(bg="white", fg="black")
            self.label3.configure(bg="white", fg="black")
            self.label4.configure(bg="white", fg="black")
            self.label5.configure(bg="white", fg="black")
            self.white = True






app = SerialPy()
app.title("SerialPy")
#app.geometry('1920x1080')
app.resizable(width=False, height=False)
app.configure(bg="black")
app.mainloop()