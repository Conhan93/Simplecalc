import tkinter as tk
#from enum import Enum


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
       
    def run_ui(self):
        """ Starts the main window loop """

        self.window.mainloop()

    def _create_display_frame(self):
        """ Creates the box or frame where the result
            will be displayed """
        self.Fdisplay = tk.Frame(master=self.window,
                                 relief='groove',bg='red')
        
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

        # skips entering an operator if calculator input already ends with an operator
        if list(filter(self.calc.get_input().endswith, self.settings.operators)):
            if _input in self.settings.operators:
                return
        # sends the input string to calculator object
        self.calc.set_input(_input)

        # updates result
        self.result_text.set(self.calc.get_input())

    def _create_buttons(self):
        """ Creates the frame that will hold the buttons """

        self.buttons = tk.Frame(master=self.window)
        self.buttons.grid(row=1, column=0, sticky="nsew")

        

        # this shit refuses to be put in a loop
        self.buttons.rowconfigure(0, weight=self.settings.button_weight)
        self.buttons.rowconfigure(1, weight=self.settings.button_weight)
        self.buttons.rowconfigure(2, weight=self.settings.button_weight)
        self.buttons.rowconfigure(3, weight=self.settings.button_weight)
        self.buttons.columnconfigure(0, weight=self.settings.button_weight)
        self.buttons.columnconfigure(1, weight=self.settings.button_weight)
        self.buttons.columnconfigure(2, weight=self.settings.button_weight)
        self.buttons.columnconfigure(3, weight=self.settings.button_weight)
        
        

        self._create_row1()
        self._create_row2()
        self._create_row3()
        self._create_row4()
        
        
    def _create_row1(self):
        

        self.bt_one = tk.Button(master=self.buttons, text="1",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width,
                                  image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("1"))
        self.bt_two = tk.Button(master=self.buttons, text="2",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, 
                                  image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("2"))
        self.bt_three = tk.Button(master=self.buttons, text="3",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width,
                                  image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("3"))
        self.bt_plus = tk.Button(master=self.buttons, text="+",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("+"))

        self.bt_one.grid(row=0,column=0)
        self.bt_two.grid(row=0,column=1)
        self.bt_three.grid(row=0,column=2)
        self.bt_plus.grid(row=0,column=3)


    def _create_row2(self):

        self.bt_four = tk.Button(master=self.buttons, text="4",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("4"))
        self.bt_five = tk.Button(master=self.buttons, text="5",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("5"))
        self.bt_six = tk.Button(master=self.buttons, text="6",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("6"))
        self.bt_subt = tk.Button(master=self.buttons, text="-",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("-"))

        self.bt_four.grid(row=1,column=0)
        self.bt_five.grid(row=1,column=1)
        self.bt_six.grid(row=1,column=2)
        self.bt_subt.grid(row=1,column=3)

    def _create_row3(self):

        self.bt_seven = tk.Button(master=self.buttons, text="7",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("7"))
        self.bt_eight = tk.Button(master=self.buttons, text="8",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("8"))
        self.bt_nine = tk.Button(master=self.buttons, text="9",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("9"))
        self.bt_multi = tk.Button(master=self.buttons, text = "X",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("*"))

        self.bt_seven.grid(row=2,column=0)
        self.bt_eight.grid(row=2,column=1)
        self.bt_nine.grid(row=2,column=2)
        self.bt_multi.grid(row=2,column=3)

    def _create_row4(self):

        self.bt_zero = tk.Button(master=self.buttons, text="0",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("0"))
        self.bt_period = tk.Button(master=self.buttons, text=".",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("."))
        self.bt_equals = tk.Button(master=self.buttons, text="=",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=self._equals)
        self.bt_div = tk.Button(master=self.buttons, text = "/",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("/"))

        self.bt_zero.grid(row=3,column=0)
        self.bt_period.grid(row=3,column=1)
        self.bt_equals.grid(row=3,column=2)
        self.bt_div.grid(row=3,column=3)

