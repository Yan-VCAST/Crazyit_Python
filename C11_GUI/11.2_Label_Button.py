from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.initWidgets()
    
    def initWidgets(self):
        w = Label(self)
        bm = PhotoImage(file='images/test.png')
        #必须用一个不会被释放的变量引用该图片，否则图片会被系统回收！！
        w.x = bm
        w['image'] = bm
        w.pack()
        okButton = Button(self, text='确定')
        okButton['background'] = 'yellow'
        okButton.pack()

app = Application()
#print(type(app.master))
app.master.title('主窗口')
app.mainloop()