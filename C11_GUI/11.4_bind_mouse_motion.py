# 为鼠标移动事件绑定事件处理方法

from tkinter import *

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    
    def initWidgets(self):
        lb = Label(self.master, width=40, height=3, bg='lightgreen', font=('Times',20))
        lb.pack()
        #为鼠标移动事件绑定事件处理方法
        lb.bind('<Motion>', self.motion)
        #为按住左键时的鼠标移动事件绑定事件处理方法
        lb.bind('<B1-Motion>', self.press_motion)
        
        self.show = Label(self.master, width=38, height=1, bg='white', font=('Courier New',20))
        self.show.pack()

    def motion(self, event):
        self.show['text'] = '鼠标移动到：（%s  %s）' % (event.x, event.y)
        return
    
    def press_motion(self, event):
        self.show['text'] = '按住鼠标的位置为：（%s  %s）' % (event.x, event.y)
        return

root = Tk()
root.title('鼠标移动事件')
App(root)
root.mainloop()