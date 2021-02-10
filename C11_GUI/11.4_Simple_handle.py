from tkinter import *

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    
    def initWidgets(self):
        self.label = Label(self.master, font=('Vedera', 20), bg='yellow', width=25)
        self.label.pack()

        '''
        colors = ('blue', 'pink', 'green', 'purple', 'red')
        for i in range(len(colors)):
            print(str('clickme'+colors[i]))
            bn[i] = Button(self.master, text=colors[i], command=self.val, width=6)
            bn[i].pack(side=LEFT)
            self.label['text'] = 'Welcome, Lucas ！'
            self.label['bg'] = colors[i]
        self.quitButton = Button(self.master, text='Quit', command=self.master.quit)
        self.quitButton.pack()
        '''
        bnblue = Button(self.master, text='Blue', command=self.clickmeblue, width=6)
        bnblue.pack(side=LEFT)
        bnpink = Button(self.master, text='Pink', command=self.clickmepink, width=6)
        bnpink.pack(side=LEFT)
        bngreen = Button(self.master, text='Green', command=self.clickmegreen, width=6)
        bngreen.pack(side=LEFT)
        bnpurple = Button(self.master, text='Purple', command=self.clickmepurple, width=6)
        bnpurple.pack(side=LEFT)
        bnred = Button(self.master, text='Red', command=self.clickmered, width=6)
        bnred.pack(side=LEFT)
        self.quitButton = Button(self.master, text='Quit', command=self.master.quit)
        self.quitButton.pack()
       
    def clickmeblue(self):
        self.label['text'] = 'Welcome, Lucas ！'
        self.label['bg'] = 'blue'
    def clickmegreen(self):
        self.label['text'] = 'Welcome, Lucas ！'
        self.label['bg'] = 'green'
    def clickmepink(self):
        self.label['text'] = 'Welcome, Lucas ！'
        self.label['bg'] = 'pink'
    def clickmepurple(self):
        self.label['text'] = 'Welcome, Lucas ！'
        self.label['bg'] = 'purple'
    def clickmered(self):
        self.label['text'] = 'Welcome, Lucas ！'
        self.label['bg'] = 'red'

root = Tk()
root.title('简单事件处理')
App(root)
root.mainloop()