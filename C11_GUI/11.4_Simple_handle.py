from tkinter import *

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    
    def initWidgets(self):
        self.label = Label(self.master, font=('Courier', 20), bg='yellow', width=25)
        self.label.pack()
        bn = Button(self.master, text='单击我', command=self.clickme)
        bn.pack()
        self.quitButton = Button(self.master, text='Quit', command=self.master.quit)
        self.quitButton.pack()
    
    def clickme(self):
        self.label['text'] = '欢迎学习Python！'
        self.label['bg'] = 'green'

root = Tk()
root.title('简单事件处理')
App(root)
root.mainloop()