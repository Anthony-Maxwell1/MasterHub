import customtkinter as ctk
from tkinter import filedialog, Canvas
from settings import *

class ImageImport(ctk.CTkFrame):
	def __init__(self, parent, import_func):
		super().__init__(master=parent, fg_color=BACKGROUND_COLOR)
		self.grid(column=0, columnspan=2, row=0, sticky='NSEW')
		self.import_func = import_func

		ctk.CTkButton(self, text='Open Image', command=self.open_dialog, corner_radius=20).pack(expand=True)

	def open_dialog(self):
		path = filedialog.askopenfile().name
		self.import_func(path)

class ImageOutput(Canvas):
	def __init__(self, parent, resize_image):
		super().__init__(master=parent, background=BACKGROUND_COLOR, bd=0, highlightthickness=0, relief='ridge')
		self.grid(row=0, column=1, sticky='NSEW', padx=10, pady=10)
		self.bind('<Configure>', resize_image)

class CloseOutput(ctk.CTkButton):
	def __init__(self, parent, close_func):
		super().__init__(master=parent, text='x', text_color=WHITE, fg_color='transparent', width=40, height=40, corner_radius=20, hover_color=CLOSE_RED, command=close_func)
		self.place(relx=0.99, rely=0.01, anchor='ne')