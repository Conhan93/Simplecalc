import tkinter as tk
#from enum import Enum


class UI:
    """ Class to hold interface related objects """

    def __init__(self, calculator):

        self.settings = calculator.settings
        self.calc = calculator.actualcalc
        
        self.window = tk.Tk()
        self.window.geometry(self.settings.main_geometry)
        self.window.maxsize(270,300)
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=4)
        self.pixel = tk.PhotoImage(width=1, height=1)

        #self.inputs = Enum('inputs','1 2 3 4 5 6 7 8 9 0 + - * /')

        
        # initiate result text
        self.result_text = tk.StringVar()
        self.result_text.set(self.calc.get_result())

        self._create_buttons()
        
        
        self._create_result_box()
        #self.results.pack()
        
        #self.buttons.pack()

        self.window.mainloop()
    def _create_calculator(self):
        """ creates the calculator """

    def _create_result_box(self):
        """ Creates the box or frame where the result
            will be displayed """
        self.Fresults = tk.Frame(master=self.window,
                                 relief='groove')
        #self.Fresults.grid(row=0)
        #self.Fresults.pack(side="top",fill="both")
        self.Fresults.grid(row=0)
        #self.Fresults.columnconfigure([0], minsize=50)
        
        

        self.lb_results = tk.Label(master=self.Fresults,
                                   textvariable=self.result_text)
        self.lb_results.config(width=10, height=5)
        self.lb_results.pack(fill="both", side="right")
    def _equals(self):

        self.calc.calculate()
        self.result_text.set(self.calc.get_result())
        print(self.result_text)
    def send_input(self, _input):
        """ function sequence when sending input to calculator """

        # skips entering an operator if calculator input already ends with an operator
        if list(filter(self.calc.get_input().endswith, self.settings.operators)):
            if _input in self.settings.operators:
                return

        self.calc.set_input(_input)
        # updates result
        self.result_text.set(self.calc.get_input())
    def _create_buttons(self):
        """ Creates the frame that will hold the buttons """

        self.buttons = tk.Frame(master=self.window)
        #self.buttons.columnconfigure([0,1,2,3], minsize=0)
        #self.buttons.rowconfigure([0,1,2,3],minsize=0)
        self.buttons.grid(row=1)

        self.buttons.rowconfigure(0, weight=1)
        self.buttons.rowconfigure(1, weight=1)
        self.buttons.rowconfigure(2, weight=1)
        self.buttons.rowconfigure(3, weight=1)

        #self.buttons.pack(side="bottom", fill="both")

        self._create_row1()
        self._create_row2()
        self._create_row3()
        self._create_row4()
        
        
    def _create_row1(self):
        self.Fbuttons_row1 = tk.Frame(master=self.buttons)

        self.bt_one = tk.Button(master=self.Fbuttons_row1, text="1",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width,
                                  image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("1"))
        self.bt_two = tk.Button(master=self.Fbuttons_row1, text="2",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, 
                                  image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("2"))
        self.bt_three = tk.Button(master=self.Fbuttons_row1, text="3",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width,
                                  image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("3"))
        self.bt_plus = tk.Button(master=self.Fbuttons_row1, text="+",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("+"))

        self.bt_one.pack(side='left')
        self.bt_two.pack(side='left')
        self.bt_three.pack(side='left')
        self.bt_plus.pack(side='left')



        #self.Fbuttons_row1.pack(side="top",fill="both")
        self.Fbuttons_row1.grid(row=0)

    def _create_row2(self):
        self.Fbuttons_row2 = tk.Frame(master=self.buttons)

        self.bt_four = tk.Button(master=self.Fbuttons_row2, text="4",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("4"))
        self.bt_five = tk.Button(master=self.Fbuttons_row2, text="5",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("5"))
        self.bt_six = tk.Button(master=self.Fbuttons_row2, text="6",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("6"))
        self.bt_subt = tk.Button(master=self.Fbuttons_row2, text="-",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("-"))

        self.bt_four.pack(side='left')
        self.bt_five.pack(side='left')
        self.bt_six.pack(side='left')
        self.bt_subt.pack(side='left')

        #self.Fbuttons_row2.pack(side="top",fill="both")
        self.Fbuttons_row2.grid(row=1)
    def _create_row3(self):
        self.Fbuttons_row3 = tk.Frame(master=self.buttons)

        self.bt_seven = tk.Button(master=self.Fbuttons_row3, text="7",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("7"))
        self.bt_eight = tk.Button(master=self.Fbuttons_row3, text="8",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("8"))
        self.bt_nine = tk.Button(master=self.Fbuttons_row3, text="9",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("9"))
        self.bt_multi = tk.Button(master=self.Fbuttons_row3, text = "X",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("*"))

        self.bt_seven.pack(side='left')
        self.bt_eight.pack(side='left')
        self.bt_nine.pack(side='left')
        self.bt_multi.pack(side='left')

        #self.Fbuttons_row3.pack(side="top",fill="both")
        self.Fbuttons_row3.grid(row=2)
    def _create_row4(self):
        self.Fbuttons_row4 = tk.Frame(master=self.buttons)

        self.bt_zero = tk.Button(master=self.Fbuttons_row4, text="0",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("0"))
        self.bt_period = tk.Button(master=self.Fbuttons_row4, text=".",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("."))
        self.bt_equals = tk.Button(master=self.Fbuttons_row4, text="=",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=self._equals)
        self.bt_div = tk.Button(master=self.Fbuttons_row4, text = "/",
                                  height=self.settings.button_height,
                                  width=self.settings.button_width, image=self.pixel,
                                  compound = "c", command=lambda: self.send_input("/"))

        self.bt_zero.pack(side='left',fill="both")
        self.bt_period.pack(side='left',fill="both")
        self.bt_equals.pack(side='left',fill="both")
        self.bt_div.pack(side='left',fill="both")

        #self.Fbuttons_row4.pack(side="top",fill="both")
        self.Fbuttons_row4.grid(row=3)

