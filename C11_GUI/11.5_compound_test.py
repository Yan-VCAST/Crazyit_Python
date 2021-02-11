from tkinter import *
from tkinter import ttk

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    
    def initWidgets(self):
        bm = PhotoImage(file = 'images/test.png')
        self.label = ttk.Label(self.master, 
            text='This is for testing!', 
            image=bm, 
            font=('StSong', 20, 'bold'), 
            foreground='red')
        self.label.bm = bm
        self.label['compound'] = None
        self.label.pack()

        f = ttk.Frame(self.master)
        f.pack(fill=BOTH, expand=YES)
        compounds = ('None', 'LEFT', 'RIGHT', 'TOP', 'BOTTOM', 'CENTER')
        #定义一个StringVar变量，用作绑定Radiobutton的变量
        self.var = StringVar()
        self.var.set('None')
        for val in compounds:
            rb = Radiobutton(f, 
                text=val, 
                padx=20, 
                variable=self.var, 
                command=self.change_compound, 
                value=val).pack(side=LEFT, anchor=CENTER)
    
    def change_compound(self):
        self.label['compound'] = self.var.get().lower()

root = Tk()
root.title('Compound测试')
App(root)
root.mainloop()