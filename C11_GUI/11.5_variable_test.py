from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    
    def initWidgets(self):
        #组件的值必须和tkinter包下的Variable子类进行绑定，而不能和普通变量绑定！
        self.st = StringVar()
        #将textvariable绑定到self.st变量
        ttk.Entry(self.master, textvariable=self.st, width=24, font=('StSong', 20, 'bold'), foreground='red').pack(fill=BOTH, expand=YES)

        f = Frame(self.master)
        f.pack()
        ttk.Button(f, text='改变', command=self.change).pack(side=LEFT)
        ttk.Button(f, text='获取', command=self.get).pack(side=LEFT)
    
    def change(self):
        books = ('green', 'red', 'blue', 'pink', 'purple', 'red')
        #改变self.st变量，与之绑定的Entry内容随之改变
        self.st.set(books[random.randint(0,5)])

    def get(self):
        messagebox.showinfo(title='输入内容', message=self.st.get())

root = Tk()
root.title('Variable测试')
App(root)
root.mainloop()