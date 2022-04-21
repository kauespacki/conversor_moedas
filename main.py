from tkinter import *
from tkinter import ttk
import requests


class Application:
	def __init__(self):
		self.root = root
		self.window()
		self.frames()
		self.coins()
		self.widgets()
		self.convert()
		self.root.mainloop()

	def window(self):
		self.root.title('')
		self.root.geometry('350x400')
		self.root.resizable(False, False)

	def frames(self):
		self.frame_0 = Frame(self.root, width=350, height=75, bg='#107db2')
		self.frame_0.place(x=0, y=0)

		self.frame_1 = Frame(self.root, width=350, height=325, bg='white')
		self.frame_1.place(x=0, y=75)

	def coins(self):
		response = requests.get('https://economia.awesomeapi.com.br/json/all')
		if response.status_code == 200:
			response = response.json()
			self.coins = ['BRL']
			for k in response.keys():
				self.coins.append(k)

	def widgets(self):
		lb_title = Label(self.frame_0, text='Currency converter', font=('arial', 20, 'bold'), fg='white', bg='#107db2')
		lb_title.place(x=175, y=37.5, anchor=CENTER)

		lb_result = Label(self.frame_1, text='', font=('arial', 16), fg='black', bg='white', width=20, height=3, relief=SOLID)
		lb_result.place(x=175, y=75, anchor=CENTER)

		lb_in = Label(self.frame_1, text='In', font=('arial', 12), fg='black', bg='white')
		lb_in.place(x=50, y=150, anchor=W)

		cbb_in = ttk.Combobox(self.frame_1, font=('arial', 12), values=self.coins, foreground='black', width=8)
		cbb_in.place(x=50, y=175, anchor=W)

		lb_for = Label(self.frame_1, text='For', font=('arial', 12), fg='black', bg='white')
		lb_for.place(x=235, y=150, anchor=E)

		cbb_for = ttk.Combobox(self.frame_1, font=('arial', 12), values=self.coins, foreground='black', width=8)
		cbb_for.place(x=300, y=175, anchor=E)

		et_amount = Entry(self.frame_1, font=('arial', 13), width=27, fg='black', bg='white', relief=SOLID, justify=CENTER, highlightthickness=1)
		et_amount.place(x=175, y=225, anchor=CENTER)

		bt_convert = Button(self.frame_1, text='Convert', font=('arial', 14, 'bold'), width=20, fg='white', bg='#107db2', overrelief=RIDGE, command=self.convert())
		bt_convert.place(x=175, y=275, anchor=CENTER)

	def convert(self):
		pass


root = Tk()
Application()
