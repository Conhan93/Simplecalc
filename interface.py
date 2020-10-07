import tkinter as tk


class UI:
    """ Class to hold interface related objects """

    def __init__(self, simpcalc):
        """ initializes GUI """

        # makes settings and calculator available to UI
        self.settings = simpcalc.settings
        self.calc = simpcalc.calc
        
        self.window = tk.Tk()
        self.window.title('Simplecalc')

        self.window.geometry(self.settings.main_geometry)
        self.window.maxsize(int(self.settings.main_width), int(self.settings.main_height))
        self.window.minsize(int(self.settings.main_width)//2, int(self.settings.main_height)//2)

        self.window.rowconfigure(0, weight=self.settings.display_frame_weight)
        self.window.rowconfigure(1, weight=self.settings.button_frame_weight)
        self.window.columnconfigure(0, weight=1)

        self.pixel = tk.PhotoImage(width=1, height=1)

        # creates the lower frame containing keyboard buttons
        # and the top frame which will display calculations
        self._create_buttons()
        self._create_display_frame()
       
    def start_loop(self):
        """ Starts the main window loop """

        self.window.mainloop()

    def _create_display_frame(self):
        """ Creates the box or frame where the result
            will be displayed """
        self.Fdisplay = tk.Frame(master=self.window,
                                 relief='groove')
        
        self.Fdisplay.grid(row=0, sticky="nsew")
        
        # initiate result text
        self.result_text = tk.StringVar()
        self.result_text.set(self.calc.get_result())
        
        # creates label that will display calculated result
        self.lb_results = tk.Label(master=self.Fdisplay,
                                   textvariable=self.result_text)
        self.lb_results.config(width=10, height=5)
        self.lb_results.pack(fill="both", side="right")
    def _equals(self):
        """ Starts a calculation and retrieves and display the result """

        self.calc.calculate()

        # updates display with result
        self.result_text.set(self.calc.get_result())

    def send_input(self, _input):
        """ function sequence when sending input to calculator """

        
        # sends the input string to calculator object
        self.calc.set_input(_input)

        # updates result
        self.result_text.set(self.calc.get_input())

    def _create_buttons(self):
        """ Creates the frame that will hold the buttons """

        self.buttons = tk.Frame(master=self.window)
        self.buttons.grid(row=1, column=0, sticky="nsew")

        

        # sets row and col config for buttons frame
        for index in range(self.settings.nr_buttons_side):
            self.buttons.rowconfigure(index, weight=self.settings.button_weight)
            self.buttons.columnconfigure(index, weight=self.settings.button_weight)
       
        # Creates all the buttons for the calculator
        # - could probably do with a refactor
        
        self.button_list = []

        self.stuff = ['1', '2', '3', '+', '4', '5', '6', '-', '7', '8',
                     '9', '*', '0', '.', '/']
        for thing in self.stuff:
            self.button_list.append(tk.Button(master=self.buttons, text=thing,
                                  height=self.settings.button_height,
                                  width=self.settings.button_width,
                                  image=self.pixel,
                                  compound = "c", command=lambda thing=thing: self.send_input(thing)))
        self.button_list.append(tk.Button(master=self.buttons, text="=",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=self._equals))
        for index, button in enumerate(self.button_list):
            button.grid(row=(index//self.settings.nr_buttons_side),
                       column=index%self.settings.nr_buttons_side)

