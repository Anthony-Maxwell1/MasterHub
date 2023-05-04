from auth import begin_auth
from calculator.calcFrame import CalculatorFrame
import customtkinter as ctk
import subprocess
import pathlib

MAIN_ROWS = 20
MAIN_COLUMNS = 20

class App(ctk.CTk):
	def __init__(self):
		

		with open("current_license.txt", "r") as f:
			f.readline()
			if f.readline() != 'None':
				super().__init__()
				self.title = 'MasterHub'
				self.rowconfigure(list(range(MAIN_ROWS)), weight=1, uniform='a')
				self.columnconfigure(list(range(MAIN_COLUMNS)), weight=1, uniform='a')
				self.resizable(False, False)

				
				CalculatorFrame(parent=self, col=0, row=0)

				self.mainloop()

	def _open(self, app, _dir=None):
		if dir != None:
			subprocess.run(f'python {pathlib.Path(__file__).parent.resolve()}\\{_dir}\\{app}')
		else:
			subprocess.run(f'python {pathlib.Path(__file__).parent.resolve()}\\{app}')

App()