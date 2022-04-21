from tkinter import *


class Application:
	def __init__(self):
		self.root = root
		self.window()
		self.root.mainloop()

	def window(self):
		self.root.title('')
		self.root.geometry('400x400')
		self.root.resizable(False, False)


root = Tk()
Application()
