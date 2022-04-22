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
		self.response = requests.get('https://economia.awesomeapi.com.br/json/all')
		if self.response.status_code == 200:
			self.response = self.response.json()
			self.coins = ['BRL']
			for k in self.response.keys():
				self.coins.append(k)

	def widgets(self):
		self.lb_title = Label(self.frame_0, text='Currency converter', font=('arial', 20, 'bold'), fg='white', bg='#107db2')
		self.lb_title.place(x=175, y=37.5, anchor=CENTER)

		self.lb_result = Label(self.frame_1, text='', font=('arial', 16), fg='black', bg='white', width=20, height=3, relief=SOLID)
		self.lb_result.place(x=175, y=75, anchor=CENTER)

		self.lb_in = Label(self.frame_1, text='In', font=('arial', 12), fg='black', bg='white')
		self.lb_in.place(x=50, y=150, anchor=W)

		self.cbb_in = ttk.Combobox(self.frame_1, font=('arial', 12), values=self.coins, foreground='black', width=8, state='readonly')
		self.cbb_in.current(0)
		self.cbb_in.place(x=50, y=175, anchor=W)

		self.lb_for = Label(self.frame_1, text='For', font=('arial', 12), fg='black', bg='white')
		self.lb_for.place(x=235, y=150, anchor=E)

		self.cbb_for = ttk.Combobox(self.frame_1, font=('arial', 12), values=self.coins, foreground='black', width=8, state='readonly')
		self.cbb_for.current(1)
		self.cbb_for.place(x=300, y=175, anchor=E)

		self.et_amount = Entry(self.frame_1, font=('arial', 13), width=27, fg='black', bg='white', relief=SOLID, justify=CENTER, highlightthickness=1)
		self.et_amount.place(x=175, y=225, anchor=CENTER)

		self.bt_convert = Button(self.frame_1, text='Convert', font=('arial', 14, 'bold'), width=20, fg='white', bg='#107db2', overrelief=RIDGE, command=self.convert)
		self.bt_convert.place(x=175, y=275, anchor=CENTER)

	def convert(self):
		self.coin_in = self.cbb_in.get()
		self.coin_for = self.cbb_for.get()
		self.amount = self.et_amount.get()

		if self.coin_in == self.coin_for:
			self.lb_result['text'] = 'Enter different currencies'
			return 0

		if len(self.amount) > 0:
			pass

		else:
			self.lb_result['text'] = 'Enter the amount'
			return 0

		try:	
			self.amount = float(self.amount)
			if self.coin_in == 'BRL':
				self.price_for = float(self.response.get(f'{self.coin_for}')['bid'])
				self.result = self.amount / self.price_for

			elif self.coin_for == 'BRL':
				self.price_in = float(self.response.get(f'{self.coin_in}')['bid'])
				self.result = self.amount * self.price_in

			else:
				self.price_in = float(self.response.get(f'{self.coin_in}')['bid'])
				self.price_for = float(self.response.get(f'{self.coin_for}')['bid'])

				self.result = (self.amount * self.price_in) / self.price_for

			self.lb_result['text'] = f'{self.coin_for} {self.result:,.7f}'
		except Exception as error:
			print(error)


root = Tk()
Application()
