#单击、双击事件绑定事件处理的方法

from tkinter import *
import sys

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    
    def initWidgets(self):
        self.show = Label(self.master, width=30, bg='white', font=('times', 20))
        self.show.pack()
        bn = Button(self.master, text='单击我或双击我')
        bn.pack(fill=BOTH, expand=YES)

        #为左键单击事件绑定处理方法
        bn.bind('<Button-1>', self.one)
        #为左键双击事件绑定处理方法
        bn.bind('<Double-1>', self.double)
    
    def one(self, event):
        self.show['text'] = '左键单击：%s' % event.widget['text']
    
    def double(self, event):
        print('左键双击，推出程序：', event.widget['text'])
        sys.exit()

root = Tk()
root.title('简单绑定bind')
App(root)
root.mainloop()