import customtkinter as ctk
from panels import *

class Menu(ctk.CTkTabview):
	def __init__(self, parent, trans_vars, color_vars, effect_vars):
		super().__init__(master=parent)
		self.grid(row=0, column=0, sticky='NSEW', pady=10, padx=10)

		self.add('Transform')
		self.add('Color')
		self.add('Effects')
		self.add('Export')

		TransformFrame(self.tab('Transform'), trans_vars)
		ColorFrame(self.tab('Color'), color_vars)
		EffectFrame(self.tab('Effects'), effect_vars)

class TransformFrame(ctk.CTkFrame):
	def __init__(self, parent, trans_vars):
		super().__init__(master=parent)
		self.pack(expand=True, fill='both')

		SliderPanel(self, 'Rotation', trans_vars['rotate'], 0, 360)
		SliderPanel(self, 'Zoom', trans_vars['zoom'], 0, 200)
		SegmentedPanel(self, 'Flip', trans_vars['flip'], FLIP_OPTIONS)

class ColorFrame(ctk.CTkFrame):
	def __init__(self, parent, color_vars):
		super().__init__(master=parent)
		self.pack(expand=True, fill='both')

		SwitchPanel(self, (color_vars['grayscale'], 'B/W'), (color_vars['invert'], 'Invert'))
		SliderPanel(self, 'Brightness', color_vars['brightness'], 0, 5)
		SliderPanel(self, 'Vibrance', color_vars['vibrance'], 0, 5)

class EffectFrame(ctk.CTkFrame):
	def __init__(self, parent, effect_vars):
		super().__init__(master=parent)
		self.pack(expand=True, fill='both')

		DropDownPanel(self, effect_vars['effect'], EFFECT_OPTIONS)
		SliderDropDownPanel('Blur', effect_vars['blur'], effect_vars['blur-type'], 0, 150, BLUR_OPTIONS_LIST)
		SliderPanel(self, 'Contrast', effect_vars['contrast'], 0, 10)
