import customtkinter as ctk
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#000000")
        self.title("")
        self.iconbitmap('empty.ico')
        self.geometry("300x100")
        self.minsize(height=100, width=300)
        self.title_bar_color()

        title_frame = ctk.CTkFrame(self, fg_color='#000000')
        distance_options = ["Miles", "Kilometers", "Nanometer", "Micrometer", "Millimeter"]
        self.input_option = ctk.StringVar()
        input_type_dropdown = ctk.CTkOptionMenu(master=title_frame, values=distance_options, command=self.convert, variable=self.input_option)
        title_label = ctk.CTkLabel(title_frame, text="to", font=ctk.CTkFont(family='Comfortaa', size=10))
        self.output_option = ctk.StringVar()
        output_type_dropdown = ctk.CTkOptionMenu(master=title_frame, variable=self.output_option, values=distance_options, command=self.convert)
        input_type_dropdown.pack(side="left", expand=True)
        title_label.pack(side="left", expand=True)
        output_type_dropdown.pack(side="left", expand=True)
        title_frame.pack(expand=True)

        input_frame = ctk.CTkFrame(self, fg_color='#000000')
        self.entry_int = ctk.IntVar()
        entry = ctk.CTkEntry(input_frame, textvariable=self.entry_int)
        button = ctk.CTkButton(input_frame, text="Convert", command=self.convert)
        entry.pack(side="left", padx=10, expand=True)
        button.pack(side="left", expand=True)
        input_frame.pack(pady=10, expand=True)

        self.output_string = ctk.StringVar()
        output_label = ctk.CTkLabel(self, text="Output", font=ctk.CTkFont(family='Comfortaa', size=15), textvariable=self.output_string)
        output_label.pack(pady=5, expand=True)

        self.mainloop()

    def title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = 0x00000000
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
        except:
            pass

    def convert(self):
        Input = self.entry_int.get()
        input_type = self.input_option.get()
        output_type = self.output_option.get()
        if input_type == output_type:
            self.output_string.set(Input)
        elif input_type == "Miles" and output_type == "Kilometers":
            self.output_string.set(Input * 1.609344)
        elif input_type == "Kilometers" and output_type == "Miles":
            self.output_string.set(Input / 1.609344)
        elif input_type == "Nanometer" and output_type == "Micrometer":
            self.output_string.set(Input / 1000)
        elif input_type == "Micrometer" and output_type == "Nanometer":
            self.output_string.set(Input * 1000)
        elif input_type == "Miles" and output_type == "Nanometer":
            self.output_string.set(Input * 1.609e+12)
        elif input_type == "Nanometer" and output_type == "Miles":
            self.output_string.set(Input / 1.609e+12)
        elif input_type == "Miles" and output_type == "Micrometer":
            self.output_string.set(Input * 1.609e+9)
        elif input_type == "Micrometer" and output_type == "Miles":
            self.output_string.set(Input / 1.609e+9)
        elif input_type == "Kilometer" and output_type == "Nanometer":
            self.output_string.set(Input * 1e+12)
        elif input_type == "Nanometer" and output_type == "Kilometer":
            self.output_string.set(Input / 1e+12)
        elif input_type == "Kilometer" and output_type == "Micrometer":
            self.output_string.set(Input * 1e+9)
        elif input_type == "Micrometer" and output_type == "Kilometer":
            self.output_string.set(Input / 1e+9)
        elif input_type == "Mile" and output_type == "Millimeter":
            self.output_string.set(Input * 1.609e+6)
        elif input_type == "Millimeter" and output_type == "Mile":
            self.output_string.set(Input / 1.609e+6)
        elif input_type == "Kilometer" and output_type == "Millimeter":
            self.output_string.set(Input * 1e+6)
        elif input_type == "Millimeter" and output_type == "Kilometer":
            self.output_string.set(Input / 1e+6)
        elif input_type == "Nanometer" and output_type == "Millimeter":
            self.output_string.set(Input * 1e+6)
        elif input_type == "Millimeter" and output_type == "Nanometer":
            self.output_string.set(Input / 1e+6)
        elif input_type == "Micrometer" and output_type == "Millimeter":
            self.output_string.set(Input / 1000)
        elif input_type == "Millimeter" and output_type == "Micrometer":
            self.output_string.set(Input * 1000)

App()