import numpy as np 
from tkinter.ttk import Frame, Button,Label
from tkinter import Tk, BOTH, Menu
import tkinter.messagebox as mbox
class Execute(Frame):
	def __init__(self,parent):
		Frame.__init__(self,parent)
		self.parent=parent
		self.unitUI()

	def unitUI(self):
		self.parent.title("phan mem thu nghiem")
		self.pack()
		menuBar=Menu(self.parent)
		self.parent.config(menu=menuBar)
		filemenu=Menu(menuBar)
		filemenu.add_command(label="phim tam li tinh cam",command=self.onclick)
		filemenu.add_command(label="phim hanh dong",command=self.onclick)
		filemenu.add_command(label="phim vien tuong",command=self.onclick)
		filemenu.add_command(label="phim con heo",command=self.onclick)
		menuBar.add_cascade(label="xem phim",menu=filemenu
                                    )
	def onclick(self):
		mbox.askquestion("may bi ham ak")
root=Tk()
root.geometry("300x150+100+100")
app= Execute(root)
root.mainloop()




