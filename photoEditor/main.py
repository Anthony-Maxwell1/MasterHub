import customtkinter as ctk
import PIL
from settings import *
from image_widgets import *
from menu import *
from PIL import Image, ImageTk, ImageOps, ImageEnhance, ImageFilter
from CTkMessagebox import CTkMessagebox
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

class App(ctk.CTk):
	def __init__(self):
		super().__init__(fg_color='#000000')
		ctk.set_appearance_mode('dark')
		self.geometry('1000x600')
		self.minsize(800, 500)
		self.title('')
		self.iconbitmap('images/empty.ico')
		self.title_bar_color()

		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=2, uniform='a')
		self.columnconfigure(1, weight=6, uniform='a')

		self.init_parameters()

		self.image_width = 0
		self.image_height = 0
		self.canvas_width = 0
		self.canvas_height = 0

		self.image_import = ImageImport(self, self.import_image)

		self.is_saved = True
		self.project_is_saved = True

		self.mainloop()

	def init_parameters(self):
		self.trans_vars = {'rotate': ctk.DoubleVar(value=ROTATE_DEFAULT), 'zoom': ctk.DoubleVar(value=ZOOM_DEFAULT), 'flip': ctk.StringVar(value=FLIP_OPTIONS[0])} 
		self.color_vars = {'brightness': ctk.DoubleVar(value=BRIGHTNESS_DEFAULT), 'grayscale': ctk.BooleanVar(value=GRAYSCALE_DEFAULT), 'invert': ctk.BooleanVar(value=INVERT_DEFAULT), 'vibrance': ctk.DoubleVar(value=VIBRANCE_DEFAULT)}
		self.effect_vars = {'blur': ctk.DoubleVar(value=BLUR_DEFAULT), 'blur-type': ctk.StringVar(value=BLUR_TYPE_DEFAULT),'contrast': ctk.IntVar(value=CONTRAST_DEFAULT), 'effect': ctk.StringVar(value=EFFECT_OPTIONS[0])}

		for var in list(self.trans_vars.values()) + list(self.color_vars.values()) + list(self.effect_vars.values()):
			var.trace('w', self.manipulate_image)

	def manipulate_image(self, *args):
		self.is_saved = False
		self.project_is_saved = False
		self.image = self.original

		self.image = self.image.rotate(self.trans_vars['rotate'].get())

		self.image = ImageOps.crop(image=self.image, border=self.trans_vars['zoom'].get())

		if self.trans_vars['flip'].get() == 'X':
			self.image = ImageOps.mirror(self.image)
		elif self.trans_vars['flip'].get() == 'Y':
			self.image = ImageOps.flip(self.image)
		elif self.trans_vars['flip'].get() == 'Both':
			self.image = ImageOps.mirror(self.image)
			self.image = ImageOps.flip(self.image)

		brightness_enhancer = ImageEnhance.Brightness(self.image)
		self.image = brightness_enhancer.enhance(self.color_vars['brightness'].get())
		vibrance_enhancer = ImageEnhance.Color(self.image)
		self.image = vibrance_enhancer.enhance(self.color_vars['vibrance'].get())

		if self.color_vars['grayscale'].get():
			self.image = ImageOps.grayscale(self.image)

		if self.color_vars['invert'].get():
			self.image = ImageOps.invert(self.image)

		self.image = self.image.filter(BLUR_OPTIONS.get(self.effect_vars['blur-type'].get())(int(self.effect_vars['blur'].get())))
		self.image = self.image.filter(ImageFilter.UnsharpMask(self.effect_vars['contrast'].get()))

		self.place_image()

	def title_bar_color(self):
		try:
			HWND = windll.user32.GetParent(self.winfo_id())
			DWMWA_ATTRIBUTE = 35
			COLOR = 0x00000000
			windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
		except:
			pass

	def import_image(self, path):
		try:
			self.original = Image.open(path)
			self.image = self.original
			self.image_ratio = self.image.size[0] / self.image.size[1]
			self.image_tk = ImageTk.PhotoImage(self.image)
			self.image_import.grid_forget()
			self.image_output = ImageOutput(self, self.resize_image)
			self.close_button = CloseOutput(self, self.close_edit)
			self.menu = Menu(self, self.trans_vars, self.color_vars, self.effect_vars)
		except PIL.UnidentifiedImageError:
			msg = CTkMessagebox(title="Error", message="This program only supports image file types like png and jpg.", icon="cancel", option_1="More Info", option_2="Cancel")

			if msg.get() == "More Info":
				msg = CTkMessagebox(title="More Info", message=f"""PIL.UnidentifiedImageError: Cannot identify image file '{path}'
					This means that you have opened an invalid file type that is not an image.""")

	def resize_image(self, event):
		canvas_ratio = event.width / event.height

		self.canvas_width = event.width
		self.canvas_height = event.height

		if canvas_ratio > self.image_ratio:
			self.image_height = int(event.height)
			self.image_width = int(self.image_height * self.image_ratio)
		else:
			self.image_width = int(event.width)
			self.image_height = int(self.image_width / self.image_ratio)

		self.place_image()

	def place_image(self):
		self.image_output.delete('all')
		resized_image = self.image.resize((self.image_width, self.image_height))
		self.image_tk = ImageTk.PhotoImage(resized_image)
		self.image_output.create_image(self.canvas_width / 2, self.canvas_height / 2, image=self.image_tk)

	def close_edit(self):
		if not self.is_saved:
			msg = CTkMessagebox(title="Exit without saving?", message="Are you sure you would like to quit the current image being edited without saving?", icon="warning", option_1="Yes", option_2="Cancel")
			if msg.get() == "Yes":
				self.image_output.grid_forget()
				self.close_button.place_forget()
				self.menu.grid_forget()

				self.image_import = ImageImport(self, self.import_image)
		elif not self.project_is_saved:
			msg = CTkMessagebox(title="Exit without saving as project?", message="Are you sure you would like to quit the current image being edited without saving it as a project? You will NOT be able to revert changes after you quit unless you save it as a project. You will also not be able to make anymore edits on the image without the other changes affecting the result.", icon="warning", option_1="Yes", option_2="Cancel")
			if msg.get() == "Yes":
				self.image_output.grid_forget()
				self.close_button.place_forget()
				self.menu.grid_forget()

				self.image_import = ImageImport(self, self.import_image)
		else:
			self.image_output.grid_forget()
			self.close_button.place_forget()
			self.menu.grid_forget()

			self.image_import = ImageImport(self, self.import_image)

App()