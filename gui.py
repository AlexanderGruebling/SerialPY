import tkinter as tk
from tkinter import ttk
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
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Startseite", font=LARGE_FONT)
        ##label.pack(pady=10, padx=10)
        label.grid(row=0, column=0, padx='5', pady='5', sticky='ew')
        label.config(height=1,width=25)
        button = tk.Button(self, text="Empfangen",
                           command=lambda: controller.show_frame(Empfangen))
        button.config(height = 1, width=40)
        ##button.pack()
        button.grid(row=1, column=0, padx='5', pady='5', sticky='ew')
        button2 = tk.Button(self, text="Senden",
                            command=lambda: controller.show_frame(Senden))
        ##button2.pack()
        button2.grid(row=2, column=0, padx='5', pady='5', sticky='ew')
        button3 = tk.Button(self, text="Schließen",
                            command=self.client_exit)
        button3.place(x=0, y=0)
        button3.grid(row=3, column=0, padx='5', pady='5', sticky='ew')


    def client_exit(self):
        exit()


class Empfangen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Empfangen", font=LARGE_FONT)
        label.grid(row=0, column=0, padx='5', pady='5', sticky='ew')

        ##label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Startseite",
                           command=lambda: controller.show_frame(StartPage))

        ##button1.pack()
        button1.grid(row=1, column=0, padx='20', pady='5', sticky='ew')
        separator = ttk.Separator(self, orient="vertical")
        separator.grid(column=2, row=1, rowspan=3, sticky='ns')
        button2 = tk.Button(self, text="Senden",
                            command=lambda: controller.show_frame(Senden))
        button2.grid(row=2, column=0, padx='5', pady='5', sticky='ew')

        ##button2.pack()


class Senden(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Senden", font=LARGE_FONT)
        label.config(anchor='se')
        label.grid(row=0, column=0, padx='5', pady='5', sticky='ew')
        label2 = tk.Label(self, text="Message:")
        label2.grid(row=1, column=0, padx='5', pady='5', sticky='ew')

        e1 = ttk.Entry(self)
        e1.grid(row=1, column=1, padx='5', pady='5', sticky='ew')
        button1 = tk.Button(self, text="Startseite",
                            command=lambda: controller.show_frame(StartPage))

        button1.grid(row=2, column=0, padx='5', pady='5', sticky='ew')
        button2 = tk.Button(self, text="Empfangen",
                            command=lambda: controller.show_frame(Empfangen))
        button2.grid(row=3, column=0, padx='5', pady='5', sticky='ew')




app = SerialPy()
app.geometry('300x200')
app.resizable(width=False, height=False)
app.configure(bg="black")
app.mainloop()