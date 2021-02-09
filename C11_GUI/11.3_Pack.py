from tkinter import *

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    
    def initWidgets(self):
        fm1 = Frame(self.master)
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)
        Button(fm1, text='第一个').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='第二个').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='第三个').pack(side=TOP, fill=X, expand=YES)

        fm2 = Frame(self.master)
        fm2.pack(side=LEFT, padx=10, expand=YES)
        Button(fm2, text='第一个').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='第二个').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='第三个').pack(side=RIGHT, fill=Y, expand=YES)

        fm3 = Frame(self.master)
        fm3.pack(side=RIGHT, padx=10, fill=BOTH, expand=YES)
        Button(fm3, text='第一个').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='第二个').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='第三个').pack(side=BOTTOM, fill=Y, expand=YES)

root = Tk()
root.title('Pack布局')
display = App(root)
root.mainloop()