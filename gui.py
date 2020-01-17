import tkinter as tk
from tkinter import ttk
import serial

LARGE_FONT = ("Verdana", 12)
com1 = None
com2 = None

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
        print(cont.__name__)
        frame.tkraise()
        if cont.__name__ == 'Empfangen':
            self.ready()

    def ready(self):
        baudRate = 9600
        dataBits = 8
        stopBits = 2
        parity = 1
        '''
        com1 = ComPort('COM4', baudRate, dataBits, 1, stopBits, 'N')
        thread1 = threading.Thread(target=com1.read_from_com_port, args=())
        thread1.start()
        com2 = ComPort('COM2', baudRate, dataBits, 1, stopBits, 'N')
        thread2 = threading.Thread(target=com2.read_from_com_port, args=())
        thread2.start()
        '''
        #com1 = serial.Serial('COM4', 9600, timeout=0.5)




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

        for i in range(len(testdaten2)):
            column = 0
            if testdaten2[i][1] == "A":
                column = 0
            if testdaten2[i][1] == "B":
                column = 1
            self.name = tk.Label(self.nachrichten, text={testdaten2[i]}, font=LARGE_FONT)
            self.name.grid(row=i, column=column)

        self.button2 = tk.Button(self, text="Senden",
                            command=lambda: controller.show_frame(Senden))
        self.button2.grid(row=0, column=2, padx='5', pady='5', sticky='ew')
        self.button3 = tk.Button(self, text="Color-Theme wechseln",
                                 command=self.colorChange)
        self.button3.grid(row=3, column=0, padx='5', pady='5', sticky='ew')
        self.label6 = tk.Label(self, text="Baud-Rate:")
        self.label6.grid(row=5, column=0, padx='5', pady='5', sticky='ew')
        self.label6.config(height=1, width=5)
        self.e2 = ttk.Entry(self, width=1)
        self.e2.grid(row=5, column=1, padx='5', pady='5', sticky='ew')
        self.label7 = tk.Label(self, text="Stopbits:")
        self.label7.grid(row=5, column=2, padx='5', pady='5', sticky='ew')
        self.label7.config(height=1, width=5)
        self.e3 = ttk.Entry(self, width=5)
        self.e3.grid(row=5, column=3, padx='5', pady='5', sticky='ew')
        self.label8 = tk.Label(self, text="Databits:")
        self.label8.grid(row=5, column=4, padx='5', pady='5', sticky='ew')
        self.label8.config(height=1, width=5)
        self.e4 = ttk.Entry(self, width=5)
        self.e4.grid(row=5, column=5, padx='5', pady='5', sticky='ew')
        self.button4 = tk.Button(self, text="Refresh",
                                 command=self.refresh)
        self.button4.grid(row=4, column=0, padx='5', pady='5', sticky='ew')
        self.refresh()

        self.label6 = tk.Label(self, text="Baud-Rate:")
        self.label6.grid(row=6, column=0, padx='5', pady='5', sticky='ew')
        self.label6.config(height=1, width=5)
        self.e5 = ttk.Entry(self, width=1)
        self.e5.grid(row=6, column=1, padx='5', pady='5', sticky='ew')
        self.label7 = tk.Label(self, text="Stopbits:")
        self.label7.grid(row=6, column=2, padx='5', pady='5', sticky='ew')
        self.label7.config(height=1, width=5)
        self.e6 = ttk.Entry(self, width=5)
        self.e6.grid(row=6, column=3, padx='5', pady='5', sticky='ew')
        self.label8 = tk.Label(self, text="Databits:")
        self.label8.grid(row=6, column=4, padx='5', pady='5', sticky='ew')
        self.label8.config(height=1, width=5)
        self.e7 = ttk.Entry(self, width=5)
        self.e7.grid(row=6, column=5, padx='5', pady='5', sticky='ew')

        self.button5 = tk.Button(self, text="Submit", command=self.createCOMs)
        self.button5.grid(row=6, column=6, padx=5, pady=5, sticky='ew')

    def refresh(self):

        for i in range(len(testdaten2)):
            print("ABC")
            column = 0
            if testdaten2[i][1] == "A":
                print("links")
                column = 0
            if testdaten2[i][1] == "B":
                print("rechts")
                column = 1
            self.name = tk.Label(self.nachrichten, text={testdaten2[i]}, font=LARGE_FONT)

            self.name.grid(row=i, column=column)
        self.after(500, self.refresh)

    def createCOMs(self):
        global com1
        global com2
        print('test')
        try:
            com1 = serial.Serial('COM1', baudrate=self.e2.get(), timeout=0.5) # , stopbits=self.e3.get(), bytesize=self.e4.get()
            # com1.stopbits = self.e3.get()
            # com1.bytesize = self.e4.get()
            com2 = serial.Serial('COM6', baudrate=self.e5.get(), timeout=0.5) # , stopbits=self.e6.get(), bytesize=self.e7.get()
            # com2.stopbits = self.e6.get()
            # com2.bytesize = self.e7.get()
        except serial.SerialException:
            print('king')
            com1 = None
            com2 = None

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


def read(com1, com2):
    com1data = com1.readline()
    com2data = com2.readline()
    if com1data is not b'':
        testdaten2.append((str(com1data), "A"))
        # print(testdaten2)
    if com2data is not b'':
        testdaten2.append((str(com2data), "B"))
        # print(testdaten2)


#testdaten2 = [("ABC","A"),("123","B"),("DEF","B"),("XYZ","A")]
testdaten2 = []
app = SerialPy()
app.title("SerialPy")
#app.geometry('1920x1080')
app.resizable(width=True, height=True)
app.configure(bg="black")
while True:
    # app.update_idletasks()
    if com1 is not None and com2 is not None:
        read(com1, com2)
        print(com1.baudrate)
    else:
        print('kek')
    app.update()
